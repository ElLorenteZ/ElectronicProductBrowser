from model.Product import Product
from web_scrappers.WebScrapper import WebScrapper
from bs4 import BeautifulSoup


class AllegroWebScrapper(WebScrapper):

    def __init__(self, link):
        elements = self.get_raw_elements(link, element='div', classes='mpof_ki myre_zn _9c44d_1Hxbq')
        for element in elements:
            self.parse_element(element)

    def parse_element(self, element):
        bs = BeautifulSoup(element)
        title = bs.find('a', class_='_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY m9qz_yq')
        name = title.get_text().upper()
        url = title.get('href')
        price = float(bs.find('span', class_='_1svub _lf05o').get_text().upper().replace("zł", "").strip())
        self.products.append(Product(name, price, url))


