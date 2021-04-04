from Config import configure_session
from bs4 import BeautifulSoup

from link_generators.OleOleLinkGen import SHOP_NAME
from model.Product import Product


def get_products(links):
    products = list()
    for link in links:
        pageProducts = get_products_page(link)
        products.extend(pageProducts)
    return products


def get_products_page(link):
    products = list()
    elements = get_raw_elements(link, 'div', 'product-row')
    for element in elements:
        product = parse_single_element(element)
        if product is not None:
            products.append(product)
    return products


def parse_single_element(element):
    try:
        title = element.find('a', class_='js-save-keyword')
        if title is None:
            raise RuntimeError
        name = title.get_text().strip().upper()
        url = 'https://www.oleole.pl' + title.get('href')
        priceElement = element.find('div', class_='price-normal selenium-price-normal')
        if priceElement is not None:
            price = float(priceElement
                          .get_text()
                          .replace("zł", "")
                          .strip()
                          .replace(',', '.')
                          .replace(u'\xa0', u' ')
                          .replace(" ", ""))
        else:
            raise RuntimeError("Price element not found. Element skipped.")
        return Product(name, price, url, SHOP_NAME)
    except RuntimeError:
        return None


def get_raw_elements(link, element, classes):
    session = configure_session()
    response = session.get(link)
    bs = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    return bs.find_all(element, class_=classes)
