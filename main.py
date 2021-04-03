from link_generators.AllLinksGenerator import AllLinksGenerator

PRODUCT_NAME = "HyperX Cloud"

if __name__ == "__main__":
    allLinkGenerator = AllLinksGenerator(PRODUCT_NAME)
    for linkEntry in allLinkGenerator.links:
        print("%s\t: %s" % (linkEntry.shop, linkEntry.link))
