import feedparser
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from config import RSS_SOURCES, BOURUGE_RELEVANCE, MONITORING_CONFIG
import hashlib
import json
import os
import re

class RSSFeedParser:
    def __init__(self):
        self.sent_articles_tracker = None
        try:
            from sent_articles_tracker import SentArticlesTracker
            self.sent_articles_tracker = SentArticlesTracker()
        except ImportError:
            print("Warning: SentArticlesTracker not available, duplicate prevention disabled")
    
    def fetch_and_filter_news(self) -> List[Dict]:
        """Fetch and filter news from RSS feeds with enhanced quality control"""
        all_articles = []
        
        for source_name, feed_url in RSS_SOURCES.items():
            try:
                print(f"Fetching from {source_name}...")
                articles = self.fetch_feed(feed_url, source_name)
                filtered_articles = self.filter_articles(articles, source_name)
                all_articles.extend(filtered_articles)
                print(f"✅ {source_name}: {len(filtered_articles)} relevant articles")
            except Exception as e:
                print(f"❌ Error fetching from {source_name}: {e}")
        
        # Remove duplicates
        unique_articles = self.remove_duplicates(all_articles)
        print(f"📊 Found {len(unique_articles)} unique relevant articles")
        
        # Apply quality control
        quality_articles = self.apply_quality_control(unique_articles)
        print(f"🎯 Quality articles: {len(quality_articles)}")
        
        return quality_articles
    
    def fetch_feed(self, feed_url: str, source_name: str) -> List[Dict]:
        """Fetch articles from a single RSS feed"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(feed_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            articles = []
            
            for entry in feed.entries:
                article = {
                    'title': self.clean_text(entry.get('title', '')),
                    'summary': self.clean_text(entry.get('summary', entry.get('description', ''))),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'source': source_name,
                    'category': 'Logistics Intelligence'
                }
                articles.append(article)
            
            return articles
            
        except Exception as e:
            print(f"Error fetching feed from {source_name}: {e}")
            return []
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text content"""
        if not text:
            return ""
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove special characters that might cause issues
        text = re.sub(r'[^\w\s\-.,;:!?()[\]{}"\'/]', '', text)
        
        return text
    
    def filter_articles(self, articles: List[Dict], source_name: str) -> List[Dict]:
        """Filter articles based on relevance criteria with enhanced logic"""
        relevant_articles = []
        
        for article in articles:
            if self.is_borouge_relevant(article):
                # Enhance article with actionable summary
                enhanced_article = self.enhance_article(article)
                relevant_articles.append(enhanced_article)
        
        return relevant_articles
    
    def is_borouge_relevant(self, article: Dict) -> bool:
        """Enhanced relevance check with stricter criteria"""
        title = article.get('title', '').lower()
        summary = article.get('summary', '').lower()
        content = f"{title} {summary}"
        
        # Check blacklist first (filter out)
        blacklist = BOURUGE_RELEVANCE.get('blacklist', [])
        for blacklist_term in blacklist:
            if blacklist_term.lower() in content:
                print(f"❌ BLACKLISTED: ['{blacklist_term}']")
                return False
        
        # Enhanced relevance logic
        entities = BOURUGE_RELEVANCE.get('entities', [])
        locations = BOURUGE_RELEVANCE.get('ports_routes', [])
        impacts = BOURUGE_RELEVANCE.get('impact_events', [])
        
        # Check for entities + impact OR locations + impact
        entities_found = [entity for entity in entities if entity.lower() in content]
        locations_found = [location for location in locations if location.lower() in content]
        impacts_found = [impact for impact in impacts if impact.lower() in content]
        
        # Debug output
        print(f"👥 Entities found: {entities_found}")
        print(f"📍 Locations found: {locations_found}")
        print(f"💥 Impacts found: {impacts_found}")
        
        # Enhanced relevance criteria
        entity_impact_match = len(entities_found) > 0 and len(impacts_found) > 0
        location_impact_match = len(locations_found) > 0 and len(impacts_found) > 0
        
        is_relevant = entity_impact_match or location_impact_match
        
        print(f"✅ Relevant: {is_relevant} (Entity+Impact: {entity_impact_match}, Location+Impact: {location_impact_match})")
        
        return is_relevant
    
    def enhance_article(self, article: Dict) -> Dict:
        """Enhance article with actionable summary and key information"""
        title = article.get('title', '')
        summary = article.get('summary', '')
        content = f"{title} {summary}"
        
        # Extract key information
        key_entities = self.extract_key_entities(content)
        key_locations = self.extract_key_locations(content)
        key_impacts = self.extract_key_impacts(content)
        
        # Create actionable summary
        actionable_summary = self.create_actionable_summary(title, summary, key_entities, key_locations, key_impacts)
        
        # Enhanced article
        enhanced_article = article.copy()
        enhanced_article['summary'] = actionable_summary
        enhanced_article['key_entities'] = key_entities
        enhanced_article['key_locations'] = key_locations
        enhanced_article['key_impacts'] = key_impacts
        enhanced_article['actionable'] = len(key_impacts) > 0
        
        return enhanced_article
    
    def extract_key_entities(self, content: str) -> List[str]:
        """Extract key entities from content"""
        entities = BOURUGE_RELEVANCE.get('entities', [])
        found_entities = []
        
        for entity in entities:
            if entity.lower() in content.lower():
                found_entities.append(entity)
        
        return found_entities[:3]  # Limit to top 3
    
    def extract_key_locations(self, content: str) -> List[str]:
        """Extract key locations from content"""
        locations = BOURUGE_RELEVANCE.get('ports_routes', [])
        found_locations = []
        
        for location in locations:
            if location.lower() in content.lower():
                found_locations.append(location)
        
        return found_locations[:3]  # Limit to top 3
    
    def extract_key_impacts(self, content: str) -> List[str]:
        """Extract key impacts from content"""
        impacts = BOURUGE_RELEVANCE.get('impact_events', [])
        found_impacts = []
        
        for impact in impacts:
            if impact.lower() in content.lower():
                found_impacts.append(impact)
        
        return found_impacts[:3]  # Limit to top 3
    
    def create_actionable_summary(self, title: str, summary: str, entities: List[str], locations: List[str], impacts: List[str]) -> str:
        """Create actionable summary for SVP consumption"""
        # Start with the main point
        actionable_parts = []
        
        # Add key impact information
        if impacts:
            actionable_parts.append(f"Impact: {', '.join(impacts[:2])}")
        
        # Add location information
        if locations:
            actionable_parts.append(f"Location: {', '.join(locations[:2])}")
        
        # Add entity information
        if entities:
            actionable_parts.append(f"Entities: {', '.join(entities[:2])}")
        
        # Create actionable summary
        if actionable_parts:
            actionable_summary = f"{title}. {' | '.join(actionable_parts)}."
        else:
            actionable_summary = f"{title}. {summary[:200]}..."
        
        # Remove hallucination-prone phrases
        hallucination_phrases = [
            "seek solutions", "looking for solutions", "exploring options", 
            "considering measures", "working on", "addressing concerns",
            "monitoring situation", "keeping watch", "staying alert",
            "in response to", "following reports", "amid concerns"
        ]
        
        for phrase in hallucination_phrases:
            actionable_summary = actionable_summary.replace(phrase, "")
        
        # Clean up extra spaces and punctuation
        actionable_summary = re.sub(r'\s+', ' ', actionable_summary).strip()
        actionable_summary = re.sub(r'\.\s*\.', '.', actionable_summary)
        
        return actionable_summary
    
    def apply_quality_control(self, articles: List[Dict]) -> List[Dict]:
        """Apply quality control to filter out hallucination-prone content"""
        quality_articles = []
        
        for article in articles:
            if self.is_high_quality(article):
                quality_articles.append(article)
            else:
                print(f"❌ LOW QUALITY: {article.get('title', '')[:50]}...")
        
        return quality_articles
    
    def is_high_quality(self, article: Dict) -> bool:
        """Check if article meets quality standards"""
        title = article.get('title', '')
        summary = article.get('summary', '')
        content = f"{title} {summary}"
        
        # Quality criteria
        hallucination_indicators = [
            "seek solutions", "looking for solutions", "exploring options",
            "considering measures", "working on", "addressing concerns",
            "monitoring situation", "keeping watch", "staying alert",
            "in response to", "following reports", "amid concerns",
            "may affect", "could impact", "potential impact", "possible disruption"
        ]
        
        # Check for hallucination indicators
        for indicator in hallucination_indicators:
            if indicator in content.lower():
                return False
        
        # Check for specific, actionable information
        has_specific_info = (
            article.get('key_entities') or 
            article.get('key_locations') or 
            article.get('key_impacts')
        )
        
        # Check length (too short might be filler)
        min_length = 50
        if len(content) < min_length:
            return False
        
        # Check for specific numbers, dates, or named entities
        has_specifics = bool(
            re.search(r'\d+', content) or  # Numbers
            any(entity.lower() in content.lower() for entity in BOURUGE_RELEVANCE.get('entities', [])) or
            any(location.lower() in content.lower() for location in BOURUGE_RELEVANCE.get('ports_routes', []))
        )
        
        return has_specific_info and has_specifics
    
    def remove_duplicates(self, articles: List[Dict]) -> List[Dict]:
        """Remove duplicate articles based on content hash"""
        if not self.sent_articles_tracker:
            return articles
        
        seen_hashes = set()
        unique_articles = []
        
        for article in articles:
            # Create hash from title and summary
            content = f"{article.get('title', '')} {article.get('summary', '')}"
            content_hash = hashlib.md5(content.encode()).hexdigest()
            
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_articles.append(article)
        
        return unique_articles

# Standalone function for compatibility
def fetch_and_filter_news() -> List[Dict]:
    """Standalone function for fetching and filtering news"""
    parser = RSSFeedParser()
    return parser.fetch_and_filter_news()
