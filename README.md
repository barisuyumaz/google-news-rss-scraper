# Google News RSS Scraper

A lightweight Python scraper for collecting news articles from Google News RSS feeds.

This project can fetch news by Google News category, search news by keyword, parse clustered news results, and decode Google News RSS article URLs into original publisher URLs.

It is especially useful for Turkish news collection workflows, AI-based news pipelines, content automation projects, and simple news metadata extraction.

---

## Features

- Fetch news from Google News RSS by category
- Search Google News RSS by keyword
- Parse clustered category news results
- Extract news title, link, source, published date, and source domain
- Decode Google News RSS URLs into original publisher article URLs
- Supports configurable language and country settings

---

## Python Version

This project was developed using:

```bash
Python 3.14
```

Python 3.14 is recommended.

---

## Project Structure

Recommended repository structure:

```text
google-news-rss-scraper/
│
├── google_news_scraper.py
├── main.py
├── requirements.txt
└── README.md
```

## Usage

Import the scraper:

```python
from google_news_scraper import GoogleNewsScraper

scraper = GoogleNewsScraper(language="tr", country="TR")
```

The default configuration is suitable for Turkish Google News RSS results:

```python
language="tr"
country="TR"
```

You can change these values for other countries and languages.

Example:

```python
scraper = GoogleNewsScraper(language="en", country="US")
```

---

## Supported Categories

The following Google News categories are supported:

```text
NATION
WORLD
HEALTH
SPORTS
ENTERTAINMENT
TECHNOLOGY
BUSINESS
```

You can print available categories with:

```python
print(scraper.TOPICS)
```

---

## Category Search Example

```python
from google_news_scraper import GoogleNewsScraper

scraper = GoogleNewsScraper(language="tr", country="TR")

health_news = scraper.category_search("HEALTH", max_results=3)

print(health_news)
```

Example output:

```python
[
    [
        {
            "title": "Hantavirüs pandemiye dönüşecek mi?",
            "link": "https://news.google.com/rss/articles/...",
            "published_date": "Fri, 08 May 2026 03:23:00 GMT",
            "source": "TRT Haber",
            "source_domain_link": "https://www.trthaber.com"
        },
        {
            "title": "Türkiye'de hantavirüs var mı? Sağlık Bakanlığı'ndan açıklama geldi",
            "link": "https://news.google.com/rss/articles/...",
            "source": "Hürriyet"
        }
    ]
]
```

Category search returns a nested list because Google News category feeds may contain clustered news articles.

A single topic can include the main article and multiple related articles from different sources.

---

## Keyword Search Example

```python
from google_news_scraper import GoogleNewsScraper

scraper = GoogleNewsScraper(language="tr", country="TR")

ai_news = scraper.keyword_search("Yapay Zeka", max_results=3)

print(ai_news)
```

Example output:

```python
[
    {
        "title": "Üniversite bünyesinde kas sinyallerini okuyabilen yapay zeka destekli protez el geliştiriliyor",
        "link": "https://news.google.com/rss/articles/...",
        "published_date": "Fri, 08 May 2026 09:29:16 GMT",
        "source": "Anadolu Ajansı",
        "source_domain_link": "https://aa.com.tr"
    },
    {
        "title": "Yapay zeka, savunma ve konut patlamasından bu sektör kazançlı çıkacak",
        "link": "https://news.google.com/rss/articles/...",
        "published_date": "Fri, 08 May 2026 10:15:46 GMT",
        "source": "Investing.com Türkiye",
        "source_domain_link": "https://tr.investing.com"
    }
]
```

Keyword search returns a flat list of news items.

---

## Decode Google News RSS URL Example

Google News RSS article links usually point to Google News redirect URLs.

You can decode them into original publisher URLs:

```python
from google_news_scraper import GoogleNewsScraper

scraper = GoogleNewsScraper(language="tr", country="TR")

ai_news_examples = scraper.keyword_search("Yapay Zeka", max_results=3)

google_news_url = ai_news_examples[0]["link"]

original_url = scraper.get_original_source_link(google_news_url)

print(original_url)
```

Example output:

```text
https://aa.com.tr/tr/bilim-teknoloji/universite-bunyesinde-kas-sinyallerini-okuyabilen-yapay-zeka-destekli-protez-el-gelistiriliyor/3931032
```

---

## Output Formats

### Category Search Output

Category search returns a nested list:

```python
[
    [
        {
            "title": "...",
            "link": "...",
            "published_date": "...",
            "source": "...",
            "source_domain_link": "..."
        },
        {
            "title": "...",
            "link": "...",
            "source": "..."
        }
    ]
]
```

This structure is used because category results can contain clustered news items.

---

### Keyword Search Output

Keyword search returns a flat list:

```python
[
    {
        "title": "...",
        "link": "...",
        "published_date": "...",
        "source": "...",
        "source_domain_link": "..."
    }
]
```

---

## Notes

- This scraper uses Google News RSS feeds.
- Google News RSS links may not always be decoded successfully.
- Some news items may not include full source or date information.
- Category search and keyword search return different data structures.
- Category search can return clustered news items as nested lists.
- Keyword search returns a flat list of news items.
- This project does not scrape full article content from publisher websites.
- This project only collects metadata available from Google News RSS.

---

## License

You can add your preferred license.

Example:

```text
MIT License
```
