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
        """Fetch and filter news with domain lockdown and SVP-ready quality"""
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
        
        # Apply 2026 quality control with domain lockdown
        quality_articles = self.apply_2026_quality_control(unique_articles)
        print(f"🎯 2026 SVP-ready articles: {len(quality_articles)}")
        
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
        """Filter articles with 2026 risk-aware criteria and domain lockdown"""
        relevant_articles = []
        
        for article in articles:
            if self.is_2026_relevant(article) and self.is_in_correct_domain(article):
                # Enhance article with 2026 SVP summary
                enhanced_article = self.enhance_article(article)
                relevant_articles.append(enhanced_article)
        
        return relevant_articles
    
    def is_2026_relevant(self, article: Dict) -> bool:
        """2026-enhanced relevance check with new technical risks"""
        title = article.get('title', '').lower()
        summary = article.get('summary', '').lower()
        content = f"{title} {summary}"
        
        # Check blacklist first (filter out)
        blacklist = BOURUGE_RELEVANCE.get('blacklist', [])
        for blacklist_term in blacklist:
            if blacklist_term.lower() in content:
                print(f"❌ BLACKLISTED: ['{blacklist_term}']")
                return False
        
        # 2026 Enhanced entities, locations, impacts
        entities = BOURUGE_RELEVANCE.get('entities', [])
        locations = BOURUGE_RELEVANCE.get('ports_routes', [])
        
        # 2026 Enhanced impacts with new technical risks
        impacts_2026 = BOURUGE_RELEVANCE.get('impact_events', []) + [
            'GNSS', 'GPS spoofing', 'UAV', 'projectile', 'war risk surcharge', 'WRS',
            'blank sailing', 'diversion', 'Strait of Hormuz closure'
        ]
        
        # Debug output
        entities_found = [entity for entity in entities if entity.lower() in content]
        locations_found = [location for location in locations if location.lower() in content]
        impacts_found = [impact for impact in impacts_2026 if impact.lower() in content]
        
        print(f"👥 Entities found: {entities_found}")
        print(f"📍 Locations found: {locations_found}")
        print(f"💥 2026 Impacts found: {impacts_found}")
        
        # Enhanced relevance criteria
        entity_impact_match = len(entities_found) > 0 and len(impacts_found) > 0
        location_impact_match = len(locations_found) > 0 and len(impacts_found) > 0
        
        is_relevant = entity_impact_match or location_impact_match
        
        print(f"✅ 2026 Relevant: {is_relevant} (Entity+Impact: {entity_impact_match}, Location+Impact: {location_impact_match})")
        
        return is_relevant
    
    def is_in_correct_domain(self, article: Dict) -> bool:
        """Domain Lockdown: The "Bouncer" for perfect filtering"""
        content = f"{article.get('title', '')} {article.get('summary', '')}".lower()
        
        # 1. HARD BLACKLIST (The "Kill List" for things like Car Loans/Brazil/Retail)
        kill_list = [
            'car loan', 'subprime', 'consumer credit', 'retail banking',
            'brazil', 'solar farm', 'residential', 'luxury', 'supermarket',
            'automotive', 'vehicle', 'car', 'truck', 'suv', 'sedan',
            'energy price', 'oil price', 'stock market', 'share price', 'retail sales', 'consumer spending',
            'financial services', 'investment banking', 'personal finance', 'corporate earnings'
        ]
        for bad_word in kill_list:
            if bad_word in content:
                print(f"🚫 DOMAIN LOCKDOWN: ['{bad_word}'] found - BLOCKED")
                return False
        
        # 2. SECTOR WHITELIST (Must contain at least one of these core logistics concepts)
        core_sectors = [
            'maritime', 'shipping', 'port', 'terminal', 'freight',
            'petrochemical', 'polymer', 'crude', 'lng', 'tanker',
            'supply chain', 'warehouse', 'vessel', 'container'
        ]
        
        # 3. STRATEGIC WHITELIST (UAE / ADNOC / Borouge context)
        strategic_entities = ['adnoc', 'borouge', 'uae', 'abu dhabi', 'dubai', 'khalifa', 'jebel ali']
        
        # Must be EITHER a core logistics topic OR a strategic UAE entity
        has_sector = any(sector in content for sector in core_sectors)
        has_strategy = any(ent in content for ent in strategic_entities)
        
        domain_ok = has_sector or has_strategy
        
        print(f"🔍 DOMAIN CHECK: Sector={has_sector} | Strategy={has_strategy} | Domain OK: {domain_ok}")
        
        return domain_ok
    
    def enhance_article(self, article: Dict) -> Dict:
        """Enhance article with 2026 SVP-ready summary"""
        title = article.get('title', '')
        summary = article.get('summary', '')
        content = f"{title} {summary}"
        
        # Extract 2026 key information
        key_entities = self.extract_key_entities(content)
        key_locations = self.extract_key_locations(content)
        key_impacts = self.extract_2026_impacts(content)
        
        # Create 2026 SVP-ready summary
        svp_summary = self.create_2026_svp_summary(title, summary, key_entities, key_locations, key_impacts)
        
        # Enhanced article
        enhanced_article = article.copy()
        enhanced_article['summary'] = svp_summary
        enhanced_article['key_entities'] = key_entities
        enhanced_article['key_locations'] = key_locations
        enhanced_article['key_impacts'] = key_impacts
        enhanced_article['actionable'] = len(key_impacts) > 0
        enhanced_article['svp_ready'] = self.is_svp_ready(enhanced_article)
        
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
    
    def extract_2026_impacts(self, content: str) -> List[str]:
        """Extract 2026 key impacts including new technical risks"""
        impacts = BOURUGE_RELEVANCE.get('impact_events', []) + [
            'GNSS', 'GPS spoofing', 'UAV', 'projectile', 'war risk surcharge', 'WRS',
            'blank sailing', 'diversion', 'Strait of Hormuz closure'
        ]
        found_impacts = []
        
        for impact in impacts:
            if impact.lower() in content.lower():
                found_impacts.append(impact)
        
        return found_impacts[:3]  # Limit to top 3
    
    def create_2026_svp_summary(self, title: str, summary: str, entities: List[str], locations: List[str], impacts: List[str]) -> str:
        """Create 2026 SVP-ready summary with data density"""
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
        
        # Remove 2026 hallucination phrases
        hallucination_phrases_2026 = [
            "seek solutions", "monitoring situation", "hope of a swift reopening", 
            "industry sources say", "reports suggest", "exploring options",
            "considering measures", "working on", "addressing concerns",
            "keeping watch", "staying alert", "in response to", "following reports",
            "amid concerns", "may affect", "could impact", "potential impact", "possible disruption"
        ]
        
        for phrase in hallucination_phrases_2026:
            actionable_summary = actionable_summary.replace(phrase, "")
        
        # Clean up extra spaces and punctuation
        actionable_summary = re.sub(r'\s+', ' ', actionable_summary).strip()
        actionable_summary = re.sub(r'\.\s*\.', '.', actionable_summary)
        
        return actionable_summary
    
    def apply_2026_quality_control(self, articles: List[Dict]) -> List[Dict]:
        """Apply 2026 quality control with domain lockdown"""
        quality_articles = []
        
        for article in articles:
            if self.is_svp_ready(article):
                quality_articles.append(article)
            else:
                print(f"❌ NOT SVP-READY: {article.get('title', '')[:50]}...")
        
        return quality_articles
    
    def is_high_quality(self, article: Dict) -> bool:
        """Enhanced quality check for 2026 standards"""
        title = article.get('title', '')
        summary = article.get('summary', '')
        content = f"{title} {summary}"
        
        # 2026 hallucination indicators (more aggressive)
        hallucination_phrases_2026 = [
            "seek solutions", "monitoring situation", "hope of a swift reopening", 
            "industry sources say", "reports suggest", "exploring options",
            "considering measures", "working on", "addressing concerns",
            "keeping watch", "staying alert", "in response to", "following reports",
            "amid concerns", "may affect", "could impact", "potential impact", "possible disruption"
        ]
        
        # Check for hallucination indicators
        for indicator in hallucination_phrases_2026:
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
        
        return has_specifics and has_specifics
    
    def is_svp_ready(self, article: Dict) -> bool:
        """2026 SVP-ready quality check with domain lockdown"""
        content = f"{article.get('title', '')} {article.get('summary', '')}"
        
        # 2026 Quality Markers
        has_vessel_identifier = bool(re.search(r'MV\s|MT\s|vessel|tanker|container', content, re.IGNORECASE))
        has_date_time = bool(re.search(r'\d{1,2}\s(?:Mar|March|Feb|January|Feb|Febuary)', content, re.IGNORECASE))
        has_hard_data = bool(re.search(r'\d+%', content)) or bool(re.search(r'\$\d+', content))
        has_coordinates = bool(re.search(r'\d+°[NSEW]', content)) or bool(re.search(r'\d+\.\d+[NSEW]', content))
        
        # Check for UAE port/terminal focus (relaxed requirements)
        uae_port_entities = ['Khalifa Port', 'Jebel Ali Port', 'Ruwais', 'AD Ports', 'KIZAD', 'DP World']
        has_uae_port_focus = any(port.lower() in content.lower() for port in uae_port_entities)
        
        # Check for development/expansion keywords
        development_keywords = ['expansion', 'development', 'capacity increase', 'new terminal', 'infrastructure', 'modernization', 'digital transformation']
        has_development_focus = any(keyword.lower() in content.lower() for keyword in development_keywords)
        
        # Check for operational keywords
        operational_keywords = ['operations', 'efficiency', 'improved', 'reduced', 'delays', 'congestion', 'digital port operations']
        has_operational_focus = any(keyword.lower() in content.lower() for keyword in operational_keywords)
        
        # Check for any numbers (very relaxed)
        has_any_numbers = bool(re.search(r'\d+', content))
        
        # Base quality check
        base_quality = self.is_high_quality(article)
        
        # NEW: Strategic Override for UAE Infrastructure
        # If the news is about our core backyard, we lower the "Data Density" requirement.
        strategic_locations = ['kizad', 'khalifa port', 'ruwais', 'ad ports', 'dp world', 'ta\'ziz']
        strategic_actions = ['development', 'expansion', 'mou', 'memorandum', 'partnership', 'agreement', 'investment', 'deal', 'project']
        
        content_lower = f"{article.get('title', '')} {article.get('summary', '')}".lower()
        
        is_strategic_uae_news = any(loc in content_lower for loc in strategic_locations) and \
                            any(act in content_lower for act in strategic_actions)
        
        # Debug output
        print(f"🔍 2026 Quality Check:")
        print(f"   Vessel ID: {has_vessel_identifier}")
        print(f"   Date/Time: {has_date_time}")
        print(f"   Hard Data: {has_hard_data}")
        print(f"   Coordinates: {has_coordinates}")
        print(f"   UAE Port Focus: {has_uae_port_focus}")
        print(f"   Development Focus: {has_development_focus}")
        print(f"   Operational Focus: {has_operational_focus}")
        print(f"   Any Numbers: {has_any_numbers}")
        print(f"   Strategic UAE News: {is_strategic_uae_news}")
        
        # Data density calculation
        if has_uae_port_focus and (has_development_focus or has_operational_focus):
            # UAE port development/operations news - relaxed requirements
            data_density = has_any_numbers  # Just need any numbers
        elif has_uae_port_focus:
            # UAE port general news - relaxed requirements
            data_density = has_any_numbers or has_vessel_identifier or has_date_time
        else:
            # Other news - strict requirements
            data_density = (has_vessel_identifier or has_hard_data or has_coordinates)
        
        # UPDATED RETURN:
        # Keep it high quality, but pass if it's high data density OR strategic UAE growth
        is_svp_ready = base_quality and (data_density or is_strategic_uae_news)
        
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
