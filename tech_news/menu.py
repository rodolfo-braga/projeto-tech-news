import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)


def get_news_by_quantity():
    amount = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(int(amount))


def get_news_by_title():
    title = input("Digite o título:")
    return search_by_title(title)


def get_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def get_news_by_tag():
    tag = input("Digite a tag:")
    return search_by_tag(tag)


def get_news_by_category():
    category = input("Digite a categoria:")
    return search_by_category(category)


def end_script():
    return "Encerrando script"


def switch(option):
    functions = {
        0: get_news_by_quantity,
        1: get_news_by_title,
        2: get_news_by_date,
        3: get_news_by_tag,
        4: get_news_by_category,
        5: top_5_news,
        6: top_5_categories,
        7: end_script,
    }
    try:
        return functions[option]()
    except KeyError:
        return sys.stderr.write("Opção inválida\n")


# Requisito 12
def analyzer_menu():
    menu = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    try:
        option = int(input(menu))
        return print(switch(option))
    except ValueError:
        return sys.stderr.write("Opção inválida\n")
