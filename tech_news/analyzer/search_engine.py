from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    filtered_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [
        (news['title'], news['url']) for news in filtered_news
    ]


def format_date(date):
    month = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }
    aaaa, mm, dd = str(date).split('-')
    return f'{int(dd)} de {month[mm]} de {aaaa}'


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
        formatted_date = format_date(date)
        filtered_news = search_news({"timestamp": formatted_date})
        return [
            (news['title'], news['url']) for news in filtered_news
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    filtered_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [
        (news['title'], news['url']) for news in filtered_news
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
