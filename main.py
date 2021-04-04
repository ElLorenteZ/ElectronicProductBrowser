from link_generators.AllLinksGenerator import AllLinksGenerator
from web_scrappers import MoreleWebScrapper

PRODUCT_NAME = "Xiaomi Mi9"

if __name__ == "__main__":
    allLinkGenerator = AllLinksGenerator(PRODUCT_NAME)
    for linkEntry in allLinkGenerator.links:
        print("%s\t: %s" % (linkEntry.shop, linkEntry.link))
    products = MoreleWebScrapper.get_products(["https://www.morele.net/wyszukiwarka/0/0/,,0,,,,,,,,,,/1/?q=HyperX+Cloud"])
    for product in products:
        print("%s %.2f" % (product.name, product.price))
        print(product.url)
        print("------------------------------------------------------------------------")

