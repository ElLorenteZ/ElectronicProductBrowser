### Projekt zaliczeniowy z przedmiotu Języki Skryptowe
## Porównywarka produktów
Działanie programu symuluje wpisanie wprowadzonej przez użytkownika frazy w wyszukiwarce produktów na stronie 
internetowej wybranych sklepów internetowych oraz wyświetleniu użytkownikowi wskazanych produktów. 

Działanie programu jest czasochłonne, dlatego pomimo istnienia GUI w konsoli drukowane są informacje 
o postępach pracy.

#### Pakiety wykorzystane podczas realizacji projektu [pip-21.0.1]:
Dla pythona 3.9 (interpreter uruchamiany przez 'py'):
```
py -m pip install requests
py -m pip install beautifulsoup4
```
Dla wcześniejszych wersji (interpreter uruchamiany słowem 'python')
```
python -m pip install request
python -m pip install beautifulsoup4
```

1. Python requests - wykorzystywana do pracy za pomocą sesji oraz realizacji zapytań http metodą get.
   Głównym twórcą jest Kenneth Reitz, licencja Apache2.
   https://requests.readthedocs.io/_/downloads/pl/pl/latest/pdf/
2. Beautifulsoup4 - biblioteka służąca do parsowania dokumentów xml, w szczególności html. Konstruktor z tego pakietu 
   tworzy obiekt, który obudowuje dokument html ułatwiający jego przetwarzanie np. wyszukiwanie konkretnych elementów.
   Projekt założony przez Leonarda Richardson, następnie wspierany przez Tidelift oraz społeczność, licencja MIT.
   www.crummy.com/software/BeautifulSoup/
3. urllib3.util.retry, requests.adapters.HTTPAdapter - biblioteki służące do konfiguracji zapytania z wykorzystaniem sesji.
Istnieje szansa, że pojedyncze zapytanie nie zakończy się sukcesem ze względu na błąd serwera związany z chwilowym przeciążeniem.
Z tego powodu zapytania realizowane są przez skonfigurowany mechanizm sesji.
   Projekt utrzymywany przez społeczność, licencja MIT.
   https://urllib3.readthedocs.io/en/latest/
4. abc - wykorzystany jedynie do zwiększenia czytelności kodu przez oznaczenie 
   klasy abstrakcyjnej.
5. tkinter - moduł pythona wykorzystany do stworzenia graficznego interfejsu użytkownika.
6. threading - moduł pythona do programowania wielowątkowego. Zastosowano go, aby uniknąć wrażenia "zawieszania się" 
   interfejsu graficznego. Funkcje związane z GUI powinny być krótkie i szybkie. Webscrapping jest operacją 
   czasochłonną. W związku z tym w funkcji powiązanej z przyciskami GUI blokowane są niektóre elementy interfejsu, 
   tworzone oraz uruchamiane są metody pobierające dane a na koniec ponownie odblokowywane zostają elementy GUI.
   Tym sposobem czas, podczas którego są pobierane i przetwarzane dane nie jest w pętli aplikacji traktowany 
   jako czas obsługi wydarzenia naciśnięcia przycisku.
7. csv - moduł pythona wykorzystywany do zapisania danych w postaci plików csv.
8. os - moduł pythona wykorzystywany do otwarcia wygenerowanych plików csv w domyślnym programie na komputerze użytkownika.
-------
#### Sklepy, z których pobierane są dane
1. RTV Euro AGD
2. OleOle
3. Morele
-------
## Opis plików
#### Config.py
##### zawiera funkcje konfiguracyjne:
- configure_session() - zwraca obiekt Session() z pakietu requests skonfigurowany 
w taki sposób, aby mechanizm utrzymywania połączenia był wyłączony oraz 
w przypadku odpowiedzi serwera z kodem błędu z listy [500, 502, 503, 504] 
  (np. chwilowe przeciążenie serwera) dokonano powtórzenia zapytania po wskazanym czasie [0,5 s]
-------

#### link_generators/LinkGen.py
Abstrakcyjna klasa podstawowa do obiektów zarządzającymi linkami z produktami w sklepach internetowych. Stanowi szablon do klas pochodnych: MediaExpertLinkGen
##### atrybuty:
- query_string_base - szablon do URL pod, pod którym znajdują się produkty w sklepie
- separator - znak jakim zastępowana jest spacja w danym adresie URL
- page_string - łańcuch znaków dodawany do podstawowego linku używany do stronnicowania
- shop_name = nazwa sklepu
- product_url - url po przekierowaniu wyszukiwarki, pod którym w sklepie znajdują się wyniki wyszukiwania
- query_string - uzupełniony url do zapytania o konkretny produkt na konkretnej stronie
- max_pages - numer ostatniej strony z wynikiem wyszukiwania
##### metody:
- get_page_info() - pierwsze zapytanie na stronę po przygotowaniu zapytania http,
służy otrzymaniu adresu po przekierowaniu oraz otrzymania liczby stron z produktami w przypadku stronnicowania,
- get_links_list() - generuje listę linków do wszystkich podstron w konkretnym sklepie, na których znajdują się wyszukiwane produkty,
- get_last_page_number(html_content) - metoda wykorzystująca webscrapping do wyciągnięcia liczby stron z produktami w konkretnym sklepie,
metoda abstrakcyjna, gdyż jej implementacja zależy ściśle od sklepu,
  
W plikach:
 - link_generators/MoreleLinkGen.py
 - link_generators/OleOleLinkGen.py
 - link_generators/RTVEuroAGDLinkGen.py

znajdują się klasy pochodne dla klasy LinkGen zawierające implementacje metod związaną z konkretnymi sklepami.
   
#### link_generators/AllLinksGenerator.py
Plik zawiera klasę, która tworzy główny generator linków zależny od parametru config (mapy zawierającej informacje
czy dany generator linków ma być zastosowany czy nie). Klasa ta przechowuje również ostatnio użyte generatory linków 
oraz znalezione linki.

#### web_scrappers
Moduły wykorzystujące webscrapping dokumentu html otrzymanego w odpowiedzi serwera do otrzymania listy produktów.

Moduły z funkcjami:
 - web_scrappers/MoreleWebScrapper.py
 - web_scrappers/OleOleWebScrapper.py
 - web_strappers/RTVEuroAGDWebScrapper.py

zawierają funkcje służące do ekstrakcji danych z dokumentów html.
   
Wszystkie moduły zawierają następujące funkcje:
 - get_products(links) - przyjmujący listę obiektów LinkEntry, wykorzystywany na etapie testów do parsowania 
   produktów z pojedynczego sklepu,
 - get_products_page(link) - funkcja zwraca listę Produktów znajdujących się na stronie pod adresem 
   przekaznym w parametrze 'link',
 - parse_single_element(element) - funkcja przetwarzająca obiekt Beautifulsoup obudowujący fragment kodu html 
   obejmującego pojedynczy produkt na stronie oraz zwracająca obiekt klasy Product
 - get_raw_elements(link, element, classes) - funkcja przetwarzająca dokument html na listę obiektów Beautifulsoup,
   które obudowują fragmenty kodu html od znacznka 'element' z klasami 'classes', wykorzystywany do otrzymania 
   listy obiektów BeautifulSoup obudowujących fragment kodu html opisujący pojedynczy produkt.
   
#### web_scrappers/WebScrapper.py
Moduł z funkcją przetwarzającą listę obiektów typu LinkEntry na listę produktów. Na podstawie atrybutu 'shop'
obiektu LinkEntry wybierana jest odpowiednia funkcja parsująca kod html.

#### model/LinkEntry.py 
Klasa modelu danych - struktura danych składająca się z nazwy sklepu oraz adresu url.

#### model/Product.py
Klasa modelu danych - struktura danych przechowująca pojedynczy produkt.

#### gui_strings_pl.py
Miejsce gdzie zostały umieszczone wszystkie łańcuchy znaków występujące w GUI.

#### main.py
Główny skrypt zawierający graficzny interfejs użytkownika, wywołanie funkcji generujących linki 
i parsujących dane. W tym pliku zostały umieszczone funkcje obsługi przycisków.

Konfiguracja głównego okna programu o konkretnej nazwie, rozmiarze 640x480 px 
z zablokowaną możliwością jego zmiany.
```python
window = Tk()
window.title(WINDOW_TITLE)
window.geometry('640x480')
window.resizable(False, False)
```

Funkcja zapisu najtańszej oraz najdroższej opcji do pliku csv.
```python
def handle_summary():
    if len(products) > 0:
        with open(SUMMARY_CSV_FILENAME, mode='w', newline='') as file:
            cursor = csv.writer(file, delimiter=";")
            cursor.writerow(["Cheapest", str(products[0].price), products[0].name, products[0].shop, products[0].url])
            cursor.writerow(["Most expensive", str(products[-1].price), products[-1].name, products[-1].shop, products[-1].url])
        thread = Thread(target=open_summary)
        thread.start()
```

Funkcja zapisu posortowanej listy produktów do pliku csv.
```python
def handle_csvproducts():
    if len(products) > 0:
        with open(PRODUCTS_CSV_FILENAME, mode='w', newline='') as file:
            cursor = csv.writer(file, delimiter=';')
            cursor.writerow(["price", "shop", "name", "url"])
            for product in products:
                cursor.writerow([product.price, product.shop, product.name, product.url])
        thread = Thread(target=open_products)
        thread.start()
```

Obiekty podpięte pod Checkboxy w GUI odpowiadające za przechowywanie wartości typu Boolean:
```python
morele_var = BooleanVar(master=header, value=True)
oleole_var = BooleanVar(master=header, value=True)
rtveuroagd_var = BooleanVar(master=header, value=True)
```

Funkcja generująca słownik 'config' na podstawie wartości z checkboxów:
```python
def get_config():
    return {
        "Morele": morele_var.get(),
        "OleOle!": oleole_var.get(),
        "RTV Euro AGD": rtveuroagd_var.get()
    }
```

Uruchomienie okna i start głównej pętli:
```python
window.mainloop()
```

Przykładowe zlecenie wywołania funkcji w nowym wątku:
```python
def handle_input():
    global product_browser_button
    thread = Thread(target=sum_up)
    product_browser_button["state"] = DISABLED
    thread.start()

def sum_up():
    global waitLabel, product_browser_button, products
    productsList.insert(0, IN_PROGRESS)
    products = get_products_list(product_name_var.get())
    products.sort(key=lambda product: product.price)
    productsList.delete(0, productsList.size())
    for index, product in enumerate(products):
        displayedString = '{:10.2f} zł | {} | {}'.format(product.price, format(product.shop, ' ^12s'), product.name)
        productsList.insert(index, displayedString)
    product_browser_button["state"] = NORMAL
```

Sortowanie listy obiektów na podstawie wybranego pola:
```python
products.sort(key=lambda product: product.price)
```

Przejście po liście wraz z wyliczeniem:
```python
for index, product in enumerate(products):
    pass
```

Formatowanie tekstu w Listbox:
```python
displayedString = '{:10.2f} zł | {} | {}'.format(product.price, format(product.shop, ' ^12s'), product.name)
```
Opis:
- {:10.2f} - liczba zmiennoprzecinkowa wyświetlana na 10 miejscach z dwoma liczbami po przecinku
- format(string, ' ^12s') - zapis łańcucha znakowego string (s) na 12 miejscach z wyśrodkowaniem(^)

Tkinter scroll oraz Listbox:
```python
scroll = Scrollbar(app)
scroll.pack(side=RIGHT, fill=Y)
productsList = Listbox(app, yscrollcommand=scroll.set, font=("Courier New", 10), height=19)
productsList.pack(side=LEFT, fill=BOTH, expand=True)
```

Czcionka 'Courier New' została wybrana ponieważ jest dodstępna w pakiecie Tkinter oraz jest typu 'monospace'. 
Każdy znak ma dokładnie taką samą długość niezależnie od tego, czy jest to 'M', 'W' czy ' '.


Ważne parametry obiektów tkinter: 
- width, height - wysokość i szerokość podawana w liczbie znaków normalnej czcionki,
- expand - dodanie miejsca dla elementuów, jeśli element nadrzędny jest zbyt duży,
- fill - element ma wypełnić całe dostępne miejsce w poziomie (X), pionie (Y) lub obu kierunkach(BOTH),
- master - widget nadrzędny,
- variable/textvariable/.. - zmienne przechowujące wartość pola,
- padx, pady - padding elementu,
- command - funkcja callback,
- bg - kolor tła,
- fg - kolor czcionki.

#### Okno programu dla przykładowego produktu:
![OknoProgramu](https://pasteboard.co/JY7JORe.png)

#### Pliki wyjściowe:
Efektem działania programu mogą być dwa pliki wyjściowe: 
 - 'podsumowanie.csv' zawierające posortowaną po cenie listę produktów,
 - 'summary.csv' zawierające informację o najtańszym i najdroższym produkcie.

Pliki wyjściowe powstają po naciśnięciu przycisku na dole okna w momencie gdy lista 
znalezionych produktów nie jest pusta.

W folderze zostały umieszczone przykładowe pliki *.csv wygenerowane po uruchomieniu programu dla przykładowego produktu 
(słuchawek "Hyperx Cloud Alpha").

