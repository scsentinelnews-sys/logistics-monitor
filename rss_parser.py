import feedparser
import requests
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from config import RSS_SOURCES, BOURUGE_RELEVANCE, MONITORING_CONFIG, GCC_RELEVANCE
import hashlib
import json
import os

class RSSFeedParser:
    def __init__(self):
        self.sent_articles_tracker = None
        try:
            from sent_articles_tracker import SentArticlesTracker
            self.sent_articles_tracker = SentArticlesTracker()
        except ImportError:
            print("Warning: SentArticlesTracker not available, duplicate prevention disabled")
    
    def fetch_and_filter_news(self) -> List[Dict]:
        """Fetch and filter news with emergency fixes for security incidents"""
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
        
        # Apply emergency quality control
        quality_articles = self.apply_emergency_quality_control(unique_articles)
        print(f"🎯 Emergency SVP-ready articles: {len(quality_articles)}")
        
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
        """Filter articles with emergency fixes"""
        relevant_articles = []
        
        for article in articles:
            if self.is_emergency_relevant(article):
                # Enhance article with emergency summary
                enhanced_article = self.enhance_article(article)
                relevant_articles.append(enhanced_article)
        
        return relevant_articles
    
    def is_emergency_relevant(self, article: Dict) -> bool:
        """Emergency relevance check with fixes"""
        title = article.get('title', '').lower()
        summary = article.get('summary', '').lower()
        content = f"{title} {summary}"
        
        # EMERGENCY FIX: Whole-word blacklist matching
        blacklist = BOURUGE_RELEVANCE.get('blacklist', [])
        for blacklist_term in blacklist:
            # Use word boundaries to avoid "cargo" matching "car"
            if re.search(r'\b' + re.escape(blacklist_term) + r'\b', content):
                print(f"❌ BLACKLISTED: ['{blacklist_term}'] (whole-word match)")
                return False
        
        # Check GCC relevance first
        if self.is_gcc_relevant(article):
            print(f"✅ GCC RELEVANT: True")
            return True
        
        # Check other relevance
        entities = BOURUGE_RELEVANCE.get('entities', [])
        locations = BOURUGE_RELEVANCE.get('ports_routes', [])
        impacts = BOURUGE_RELEVANCE.get('impact_events', [])
        
        entities_found = [entity for entity in entities if entity.lower() in content]
        locations_found = [location for location in locations if location.lower() in content]
        impacts_found = [impact for impact in impacts if impact.lower() in content]
        
        print(f"👥 Entities found: {entities_found}")
        print(f"📍 Locations found: {locations_found}")
        print(f"💥 Impacts found: {impacts_found}")
        
        entity_impact_match = len(entities_found) > 0 and len(impacts_found) > 0
        location_impact_match = len(locations_found) > 0 and len(impacts_found) > 0
        
        is_relevant = entity_impact_match or location_impact_match
        
        print(f"✅ Relevant: {is_relevant}")
        
        return is_relevant
    
    def is_gcc_relevant(self, article: Dict) -> bool:
        """GCC relevance check with emergency fixes"""
        title = article.get('title', '').lower()
        summary = article.get('summary', '').lower()
        content = f"{title} {summary}"
        
        gcc_countries = GCC_RELEVANCE.get('countries', [])
        gcc_ports = GCC_RELEVANCE.get('ports', [])
        gcc_security_terms = GCC_RELEVANCE.get('security_terms', [])
        
        gcc_country_found = any(country in content for country in gcc_countries)
        gcc_port_found = any(port in content for port in gcc_ports)
        gcc_security_found = any(term in content for term in gcc_security_terms)
        
        # EMERGENCY FIX: Lower threshold for security incidents
        gcc_relevant = (gcc_country_found and (gcc_port_found or gcc_security_found))
        
        if gcc_relevant:
            found_countries = [country for country in gcc_countries if country in content]
            found_ports = [port for port in gcc_ports if port in content]
            found_security = [term for term in gcc_security_terms if term in content]
            
            print(f"🌍 GCC Countries found: {found_countries}")
            print(f"🏗️ GCC Ports found: {found_ports}")
            print(f"🛡️ GCC Security terms: {found_security}")
            print(f"✅ GCC RELEVANT: True")
        
        return gcc_relevant
    
    def enhance_article(self, article: Dict) -> Dict:
        """Enhance article with emergency summary"""
        title = article.get('title', '')
        summary = article.get('summary', '')
        content = f"{title} {summary}"
        
        # Create emergency summary
        emergency_summary = self.create_emergency_summary(title, summary)
        
        # Enhanced article
        enhanced_article = article.copy()
        enhanced_article['summary'] = emergency_summary
        enhanced_article['svp_ready'] = self.is_emergency_svp_ready(enhanced_article)
        
        return enhanced_article
    
    def create_emergency_summary(self, title: str, summary: str) -> str:
        """Create emergency summary for security incidents"""
        # For security incidents, the event itself is the data
        actionable_summary = f"{title}. {summary[:200]}..."
        
        # Remove hallucination phrases
        hallucination_phrases = [
            "seek solutions", "monitoring situation", "hope of a swift reopening", 
            "industry sources say", "reports suggest", "exploring options",
            "considering measures", "working on", "addressing concerns"
        ]
        
        for phrase in hallucination_phrases:
            actionable_summary = actionable_summary.replace(phrase, "")
        
        # Clean up extra spaces and punctuation
        actionable_summary = re.sub(r'\s+', ' ', actionable_summary).strip()
        actionable_summary = re.sub(r'\.\s*\.', '.', actionable_summary)
        
        return actionable_summary
    
    def apply_emergency_quality_control(self, articles: List[Dict]) -> List[Dict]:
        """Apply emergency quality control"""
        quality_articles = []
        
        for article in articles:
            if self.is_emergency_svp_ready(article):
                quality_articles.append(article)
            else:
                print(f"❌ NOT SVP-READY: {article.get('title', '')[:50]}...")
        
        return quality_articles
    
    def is_emergency_svp_ready(self, article: Dict) -> bool:
        """Emergency SVP-ready check with relaxed requirements for security"""
        content = f"{article.get('title', '')} {article.get('summary', '')}".lower()
        
        # Check if this is a security incident
        security_keywords = ['attack', 'drone', 'missile', 'explosion', 'seized', 'blocked', 'intercepted', 'uav']
        is_security_incident = any(keyword in content for keyword in security_keywords)
        
        # Check if it's GCC related
        gcc_keywords = ['oman', 'saudi', 'ksa', 'kuwait', 'qatar', 'bahrain', 'uae', 'emirates']
        is_gcc_related = any(keyword in content for keyword in gcc_keywords)
        
        # EMERGENCY FIX: For security incidents, the event itself is the data
        if is_security_incident and is_gcc_related:
            print(f"🚨 EMERGENCY SECURITY INCIDENT: {article.get('title', '')}")
            print(f"   Security: {is_security_incident} | GCC: {is_gcc_related}")
            print(f"   SVP-Ready: True (emergency override)")
            return True
        
        # Regular quality check for non-security news
        has_vessel_identifier = bool(re.search(r'MV\s|MT\s|vessel|tanker|container', content, re.IGNORECASE))
        has_hard_data = bool(re.search(r'\d+%', content)) or bool(re.search(r'\$\d+', content))
        has_date_time = bool(re.search(r'\d{1,2}\s(?:Mar|March|Feb|January|Feb|Febuary)', content, re.IGNORECASE))
        
        # Basic quality requirements
        min_length = 50
        content_length = len(f"{article.get('title', '')} {article.get('summary', '')}")
        
        is_svp_ready = (
            content_length >= min_length and
            (has_vessel_identifier or has_hard_data or has_date_time)
        )
        
        print(f"🔍 Quality Check: Vessel={has_vessel_identifier}, Data={has_hard_data}, Date={has_date_time}")
        print(f"   SVP-Ready: {is_svp_ready}")
        
        return is_svp_ready
    
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
