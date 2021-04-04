from link_generators.RTVEuroAGDLinkGen import RTVEuroAGDLinkGen
from link_generators.MoreleLinkGen import MoreleLinkGen
from link_generators.OleOleLinkGen import OleOleLinkGen
from model.LinkEntry import LinkEntry


class AllLinksGenerator:

    linkGenerators = list()
    links = list()

    def __init__(self, PRODUCT_NAME, config=None):
        self.linkGenerators = list()
        if config is None:
            config = {
                'Morele': True,
                'OleOle!': True,
                'RTV Euro AGD': True
            }
        if 'Morele' in config.keys() and config['Morele']:
            self.linkGenerators.append(MoreleLinkGen(PRODUCT_NAME))
            print("Morele link generator is active.")
        if 'OleOle!' in config.keys() and config['OleOle!']:
            self.linkGenerators.append(OleOleLinkGen(PRODUCT_NAME))
            print("OleOle! link generator is active.")
        if 'RTV Euro AGD' in config.keys() and config['RTV Euro AGD']:
            self.linkGenerators.append(RTVEuroAGDLinkGen(PRODUCT_NAME))
            print("RTV Euro AGD link generator is active.")
        self.generate_all_links()

    def generate_all_links(self):
        self.links = list()
        for generator in self.linkGenerators:
            genLinks = generator.get_links_list()
            for link in genLinks:
                self.links.append(LinkEntry(generator.shop_name, link))

