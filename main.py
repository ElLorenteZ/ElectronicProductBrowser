from link_generators.AllLinksGenerator import AllLinksGenerator
from link_generators.AllegroLinkGen import AllegroLinkGen
from web_scrappers.AllegroWebScrapper import AllegroWebScrapper

PRODUCT_NAME = "HyperX Cloud"

if __name__ == "__main__":
    allLinkGenerator = AllLinksGenerator(PRODUCT_NAME)
    for linkEntry in allLinkGenerator.links:
        print("%s\t: %s" % (linkEntry.shop, linkEntry.link))
    scrapper = AllegroWebScrapper("https://allegro.pl/listing?string=hyperx%20cloud&bmatch=cl-e2101-d3681-c3682-ele-1-1-0319&p=2")
    print("At page found: " + str(len(scrapper.products)) + " elements")
    for product in scrapper.products:
        print(product.name + " " + str(product.price))
        print(product.url)
        print("--------------------------------------------------")

