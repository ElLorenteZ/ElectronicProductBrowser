from gui_strings_pl import SEARCH_ON, WINDOW_TITLE, PRODUCT_BROWSER, PRODUCT_BROWSE, IN_PROGRESS
from link_generators.AllLinksGenerator import AllLinksGenerator
from web_scrappers import WebScrapper
from tkinter import *
from threading import Thread

PRODUCT_NAME = "Hyperx Cloud Alpha"
BG_COLOR = "#363636"
FONT_COLOR = "#C6C6C6"

window = Tk()
window.title(WINDOW_TITLE)
window.geometry('640x480')
window.resizable(False, True)

header = Frame(window, bg=BG_COLOR)
morele_var = BooleanVar(master=header, value=True)
oleole_var = BooleanVar(master=header, value=True)
rtveuroagd_var = BooleanVar(master=header, value=True)


def get_config():
    return {
        "Morele": morele_var.get(),
        "OleOle!": oleole_var.get(),
        "RTV Euro AGD": rtveuroagd_var.get()
    }


def get_products_list(product_name):
    allLinkGenerator = AllLinksGenerator(product_name, config=get_config())
    return WebScrapper.get_all_products(allLinkGenerator.links)


search_on_label = Label(master=header, text=SEARCH_ON, fg=FONT_COLOR, bg=BG_COLOR, pady=10, font=20).pack(side=TOP)
morele_checkbox = Checkbutton(master=header, text="Morele", variable=morele_var,
                              padx=50, pady=10, selectcolor=BG_COLOR, bg=BG_COLOR,
                              fg=FONT_COLOR).pack(side=LEFT)
oleole_checkbox = Checkbutton(master=header, text="OleOle!", variable=oleole_var,
                              padx=50, pady=10, selectcolor=BG_COLOR, bg=BG_COLOR,
                              fg=FONT_COLOR).pack(side=LEFT)
rtveuroagd_checkbox = Checkbutton(master=header, text="RTV Euro AGD", variable=rtveuroagd_var,
                                  padx=50, pady=10, selectcolor=BG_COLOR, bg=BG_COLOR,
                                  fg=FONT_COLOR).pack(side=LEFT)
header.pack(side=TOP, fill="x")


browser = Frame(window)
product_name_var = StringVar(master=browser, value=PRODUCT_NAME)
product_browser_label = Label(master=browser, text=PRODUCT_BROWSER, padx=10).pack(side=LEFT)
product_browser_input = Entry(browser, textvariable=product_name_var).pack(side=LEFT, fill="x", expand=True)


def handle_input():
    global product_browser_button
    thread = Thread(target=sum_up)
    product_browser_button["state"] = DISABLED
    thread.start()


product_browser_button = Button(master=browser, text=PRODUCT_BROWSE, command=handle_input, padx=20)
product_browser_button.pack(side=RIGHT)
browser.pack(side=TOP, fill=X)

scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=Y)
productsList = Listbox(window, yscrollcommand=scroll.set, font=("Courier New", 10))
productsList.pack(side=LEFT, fill=BOTH, expand=True)


def sum_up():
    global waitLabel, product_browser_button
    productsList.insert(0, IN_PROGRESS)
    products = get_products_list(product_name_var.get())
    productsList.delete(0, productsList.size())
    for index, product in enumerate(products):
        displayedString = '{:10.2f} zł | {} | {}'.format(product.price, format(product.shop, ' ^12s'), product.name)
        productsList.insert(index, displayedString)
    product_browser_button["state"] = NORMAL


window.mainloop()
