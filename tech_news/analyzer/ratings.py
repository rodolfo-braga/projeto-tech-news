from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news_sorted = sorted(news, key=lambda x: x['comments_count'], reverse=True)
    return [
        (news['title'], news['url']) for news in news_sorted[:5]
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
