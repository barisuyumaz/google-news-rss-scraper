from google_news_scraper import GoogleNewsScraper


def main():
    scraper = GoogleNewsScraper(language="tr", country="TR")

    print("Available categories:")
    print(scraper.TOPICS)

    print("\nCategory search example:")
    category_results = scraper.category_search("HEALTH", max_results=3)
    print(category_results)

    print("\nKeyword search example:")
    keyword_results = scraper.keyword_search("Yapay Zeka", max_results=3)
    print(keyword_results)

    if keyword_results:
        print("\nOriginal source URL example:")
        google_news_url = keyword_results[0]["link"]
        original_url = scraper.get_original_source_link(google_news_url)
        print(original_url)


if __name__ == "__main__":
    main()