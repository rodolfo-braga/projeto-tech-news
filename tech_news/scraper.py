import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    news_links = selector.css('.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css('a.next::attr(href)').get()
    if not next_page_link:
        return None
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    comments_count = len(selector.css('.comment').getall())
    summary = selector.xpath('string(//div[@class="entry-content"]/p)').get()
    tags = selector.css('.post-tags ul li a::text').getall()
    category = selector.css('span.label::text').get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# Referências:
# - Para selecionar o summary no requisito 4:
# https://parsel.readthedocs.io/en/latest/usage.html#using-text-nodes-in-a-condition
