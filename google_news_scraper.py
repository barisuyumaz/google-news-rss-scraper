import feedparser
import json
from bs4 import BeautifulSoup
from googlenewsdecoder import gnewsdecoder

class GoogleNewsScraper:
    def __init__(self, language="tr", country="TR"):
        # Initialize language, country, and CEID for RSS URL generation
        self.hl = language.lower()
        self.gl = country.upper()
        self.ceid = f"{self.gl}:{self.hl}"
        # Topics that Google News supports for category-based scraping
        self.TOPICS = [
            "NATION", "WORLD", "HEALTH", 
            "SPORTS", "ENTERTAINMENT", "TECHNOLOGY", "BUSINESS"
        ]


    def category_search(self, topic, max_results=10):
        # Check topic validity
        topic = topic.upper()
        if topic not in self.TOPICS:
            raise ValueError(f"Geçersiz kategori. Desteklenenler: {self.TOPICS}")
        # Build the RSS URL based on the topic and class parameters
        url = f"https://news.google.com/rss/headlines/section/topic/{topic}?hl={self.hl}&gl={self.gl}&ceid={self.ceid}"
        # Fetch and parse the RSS feed
        feed = feedparser.parse(url)
        
        news_list = []
        for entry in feed.entries[:max_results]:
            #Source and Date of first news item
            source_name = entry.source.title if 'source' in entry else "Unknown Source"
            source_domain_link = entry.source.href if 'source' in entry else "Unknown Source Link"
            published_date = entry.published if 'published' in entry else "Unknown Date"


            html_text = entry.summary
            content_tags_soup = BeautifulSoup(html_text, 'html.parser')
            if content_tags_soup.find('a'):
                similar_news_list = []

                same_news_items_a = content_tags_soup.find_all('a')
                
                # Add first news item (which is the main one) to the dictionary
                news_item = {
                "title": same_news_items_a[0].text.strip(),
                "link": same_news_items_a[0].get('href'),
                "published_date": published_date, # Only first news item has the published date and source info
                "source": source_name,
                "source_domain_link": source_domain_link
                }
                similar_news_list.append(news_item)

                #If there are more than 1 news items, it must have "li" tags.
                if len(same_news_items_a) > 1:
                    for li_tag in content_tags_soup.find_all('li')[1:]: # Skip the first one since it's already added
                        a_tag = li_tag.find('a')
                        if a_tag:
                            news_item = {
                                "title": a_tag.text.strip(),
                                "link": a_tag.get('href'),
                                "source": li_tag.find('font').text.strip() if li_tag.find('font') else "Unknown Source"
                            }
                            similar_news_list.append(news_item)
                # Add the similar news list to the news list
                news_list.append(similar_news_list)
            else:
                print(f"News source not found!: {entry.title}")
        
        return news_list

    
    # No have cluster news items like category search.
    def keyword_search(self, query, max_results=10):
        # Build the RSS URL for keyword search
        formatted_query = query.replace(" ", "+")
        url = f"https://news.google.com/rss/search?q={formatted_query}&hl={self.hl}&gl={self.gl}&ceid={self.ceid}"
        print(url)
        # Fetch and parse the RSS feed
        feed = feedparser.parse(url)
        
        news_list = []
        for entry in feed.entries[:max_results]:
            source_name = entry.source.title if 'source' in entry else "Unknown Source"
            source_domain_link = entry.source.href if 'source' in entry else "Unknown Source Link"
            published_date = entry.published if 'published' in entry else "Unknown Date"

            html_text = entry.summary
            content_tags_soup = BeautifulSoup(html_text, 'html.parser')
            if content_tags_soup.find('a'):
                same_news_items_a = content_tags_soup.find_all('a')
                
                news_item = {
                "title": same_news_items_a[0].text.strip(),
                "link": same_news_items_a[0].get('href'),
                "published_date": published_date,
                "source": source_name,
                "source_domain_link": source_domain_link
                }
                news_list.append(news_item)
        
        return news_list
    

    # Google News URLs to original URLs
    def get_original_source_link(self, url: str) -> str | None:
        try:
            result = gnewsdecoder(url, interval=1)

            if result.get("status"):
                return result.get("decoded_url")

            print("Decode error:", result.get("message"))
            return None

        except Exception as e:
            print("Exception:", e)
            return None