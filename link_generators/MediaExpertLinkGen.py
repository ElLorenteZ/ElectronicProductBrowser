"""
Robert Radzik
El-Ayachi Jr Stitou


"""
from link_generators.LinkGen import LinkGen
from bs4 import BeautifulSoup

QUERY_STRING_BASE = "https://www.mediaexpert.pl/search?query[menu_item]=&query[querystring]="
SEPARATOR = "%2520"
PAGE_STRING = "?page="
SHOP_NAME = "Media Expert"


class MediaExpertLinkGen(LinkGen):

    def __init__(self, product_name):
        super().__init__(QUERY_STRING_BASE, SEPARATOR, PAGE_STRING, SHOP_NAME, product_name)

    def get_last_page_number(self, content):
        bs = BeautifulSoup(content, 'html.parser')
        max_pages_div = bs.find('span', class_='is-total')
        if max_pages_div:
            return int(max_pages_div.get_text())
        return 1









