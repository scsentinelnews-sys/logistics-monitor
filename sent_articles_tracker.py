import json
import os
import hashlib
from datetime import datetime, timedelta
from typing import Set, Dict

class SentArticlesTracker:
    def __init__(self):
        self.sent_articles_file = 'sent_articles.json'
        self.sent_articles = self.load_sent_articles()
        print(f"🔍 Loaded {len(self.sent_articles)} sent articles")
    
    def load_sent_articles(self) -> Dict[str, str]:
        """Load sent articles from file"""
        try:
            if os.path.exists(self.sent_articles_file):
                with open(self.sent_articles_file, 'r') as f:
                    data = json.load(f)
                    # Clean old articles (older than 7 days)
                    self.clean_old_articles(data)
                    return data
            return {}
        except Exception as e:
            print(f"Error loading sent articles: {e}")
            return {}
    
    def clean_old_articles(self, data: Dict[str, str]):
        """Remove articles older than 7 days"""
        cutoff_date = datetime.now() - timedelta(days=7)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Remove old entries
        to_remove = []
        for article_id, timestamp in data.items():
            if timestamp < cutoff_str:
                to_remove.append(article_id)
        
        for article_id in to_remove:
            del data[article_id]
        
        if to_remove:
            print(f"🧹 Cleaned {len(to_remove)} old articles")
    
    def get_article_id(self, article: Dict) -> str:
        """Generate unique ID for article using hash"""
        # Use title + source + published date as unique identifier
        title = article.get('title', '').strip()
        source = article.get('source', '').strip()
        published = article.get('published', '').strip()
        
        # Create a consistent string for hashing
        article_string = f"{title}_{source}_{published}"
        
        # Generate hash ID
        hash_id = hashlib.md5(article_string.encode()).hexdigest()
        
        print(f"🆔 Generated ID: {hash_id[:12]} for: {title[:50]}...")
        
        return hash_id
    
    def is_article_sent(self, article: Dict) -> bool:
        """Check if article was already sent"""
        article_id = self.get_article_id(article)
        is_sent = article_id in self.sent_articles
        
        if is_sent:
            print(f"🚫 Article already sent: {article_id[:12]}")
        else:
            print(f"✅ New article: {article_id[:12]}")
            
        return is_sent
    
    def mark_article_sent(self, article: Dict):
        """Mark article as sent"""
        article_id = self.get_article_id(article)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.sent_articles[article_id] = timestamp
        print(f"💾 Marked as sent: {article_id[:12]} at {timestamp}")
        self.save_sent_articles()
    
    def save_sent_articles(self):
        """Save sent articles to file"""
        try:
            with open(self.sent_articles_file, 'w') as f:
                json.dump(self.sent_articles, f, indent=2)
            print(f"💾 Saved {len(self.sent_articles)} articles to {self.sent_articles_file}")
        except Exception as e:
            print(f"Error saving sent articles: {e}")
    
    def filter_new_articles(self, articles: list) -> list:
        """Filter out already sent articles"""
        print(f"🔍 Filtering {len(articles)} articles for duplicates...")
        
        new_articles = []
        for i, article in enumerate(articles):
            print(f"📄 Article {i+1}: {article.get('title', 'No title')[:50]}...")
            
            if not self.is_article_sent(article):
                new_articles.append(article)
                self.mark_article_sent(article)
            else:
                print(f"⏭️  Skipping duplicate article")
        
        print(f"📧 Result: {len(new_articles)} new articles, {len(articles) - len(new_articles)} duplicates removed")
        return new_articles
    
    def clear_all_sent_articles(self):
        """Clear all sent articles (for testing)"""
        self.sent_articles = {}
        self.save_sent_articles()
        print("🧹 Cleared all sent articles")
