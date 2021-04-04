from Config import configure_session
from bs4 import BeautifulSoup

from link_generators.MoreleLinkGen import SHOP_NAME
from model.Product import Product


def get_products(links):
    products = list()
    for link in links:
        pageProducts = get_products_page(link)
        products.extend(pageProducts)
    return products


def get_products_page(link):
    products = list()
    elements = get_raw_elements(link, 'div', 'cat-product-content')
    for element in elements:
        product = parse_single_element(element)
        if product is not None:
            products.append(product)
    return products


def parse_single_element(element):
    try:
        title = element.find('a', 'productLink')
        name = title.get_text().strip().upper()
        url = 'https://www.morele.net' + title.get('href')
        price = float(element.find('div', 'price-new')
                      .get_text()
                      .replace("zł", "")
                      .strip()
                      .replace(',', '.')
                      .replace(u'\xa0', u' ')
                      .replace(" ", ""))  #remove non breaking spaces
        return Product(name, price, url, SHOP_NAME)
    except RuntimeError:
        return None


def get_raw_elements(link, element, classes):
    session = configure_session()
    response = session.get(link)
    response.encoding = 'utf-8'
    bs = BeautifulSoup(response.content, 'html.parser')
    return bs.find_all(element, class_=classes)
