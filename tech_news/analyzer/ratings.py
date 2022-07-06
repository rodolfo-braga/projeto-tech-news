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
    news_list = find_news()
    categories = {}
    for news in news_list:
        if news['category'] not in categories:
            categories[news['category']] = 1
        categories[news['category']] += 1
    categories_sorted = sorted(
        categories, key=lambda x: categories[x], reverse=True
    )
    return [
        category for category in categories_sorted[:5]
    ]
