from link_generators.MediaExpertLinkGen import MediaExpertLinkGen
from link_generators.RTVEuroAGDLinkGen import RTVEuroAGDLinkGen
from link_generators.MoreleLinkGen import MoreleLinkGen
from link_generators.OleOleLinkGen import OleOleLinkGen

PRODUCT_NAME = "HyperX Cloud Alpha"

if __name__ == "__main__":
    mediaExpertLinkGen = MediaExpertLinkGen(PRODUCT_NAME)
    rtvEuroAGDLinkGen = RTVEuroAGDLinkGen(PRODUCT_NAME)
    moreleLinkGen = MoreleLinkGen(PRODUCT_NAME)
    oleoleLinkGen = OleOleLinkGen(PRODUCT_NAME)
    links = mediaExpertLinkGen.get_links_list()
    for link in links:
        print(link)
    links = rtvEuroAGDLinkGen.get_links_list()
    for link in links:
        print(link)
    links = moreleLinkGen.get_links_list()
    for link in links:
        print(link)
    links = oleoleLinkGen.get_links_list()
    for link in links:
        print(link)
