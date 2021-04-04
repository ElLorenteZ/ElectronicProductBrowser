from Config import configure_session
from bs4 import BeautifulSoup
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
        products.append(product)
    return products


def parse_single_element(element):
    #bs = BeautifulSoup(e, 'html.parser')
    title = element.find('a', 'productLink')
    name = title.get_text().strip().upper()
    url = 'https://www.morele.net' + title.get('href')
    price = float(element.find('div', 'price-new')
                  .get_text()
                  .replace("zł", "")
                  .strip()
                  .replace(',', '.')
                  .replace(" ", ""))
    return Product(name, price, url)


def get_raw_elements(link, element, classes):
    session = configure_session()
    response = session.get(link)
    bs = BeautifulSoup(response.content, 'html.parser')
    return bs.find_all(element, class_=classes)
