from web_scrappers import OleOleWebScrapper, MoreleWebScrapper, RTVEuroAGDWebScrapper


def get_all_products(elements):
    products = list()
    for index, element in enumerate(elements):
        if element.shop == 'OleOle!':
            products.extend(OleOleWebScrapper.get_products_page(element.link))
        elif element.shop == 'Morele':
            products.extend(MoreleWebScrapper.get_products_page(element.link))
        elif element.shop == 'RTV Euro AGD':
            products.extend(RTVEuroAGDWebScrapper.get_products_page(element.link))
        print("Scrapping page %d/%d: %s" % (index + 1, len(elements), element.link))
    return products
