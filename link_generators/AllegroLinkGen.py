from link_generators.LinkGen import LinkGen
from bs4 import BeautifulSoup

SEPARATOR = "%20"
QUERY_STRING_BASE = "https://allegro.pl/listing?string="
PAGE_STRING = "%p="
SHOP_NAME = "Allegro"


class AllegroLinkGen(LinkGen):

    def __init__(self, product_name):
        super().__init__(QUERY_STRING_BASE, SEPARATOR, PAGE_STRING, SHOP_NAME, product_name)

    def get_last_page_number(self, content):
        bs = BeautifulSoup(content, 'html.parser')
        max_pages_divs = bs.find_all('span', class_='_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE')
        if len(max_pages_divs) > 1:
            return int(max_pages_divs[-1]['data-page'])
        return 1

