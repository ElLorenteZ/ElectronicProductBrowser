#####Autorzy:
- Robert Radzik
- El-Ayachi Jr Stitou
------------
### Projekt zaliczeniowy z przedmiotu Języki Skryptowe
##Porównywarka produktów

####Pakiety wykorzystane podczas realizacji projektu [pip-21.0.1]:
1. Python requests - wykorzystywana do pracy za pomocą sesji oraz realizacji zapytań http metodą get.
```
python -m pip install request
py -m pip install request
```
2. Beautifulsoup4 - biblioteka służąca do webscrappingu.
```
python -m pip install beautifulsoup4
py -m pip install beautifulsoup4
```
3. urllib3.util.retry, requests.adapters.HTTPAdapter - biblioteki służące do konfiguracji zapytania z wykorzystaniem sesji.
Istnieje szansa, że pojedyncze zapytanie nie zakończy się sukcesem ze względu na błąd serwera związany z chwilowym przeciążeniem.
Z tego powodu zapytania realizowane są przez skonfigurowany mechanizm sesji.
4. abc - zwiększenie czytelności kodu przez oznaczenie klasy abstrakcyjnej.
-------
####Sklepy, z których pobieramy dane
1. RTV Euro AGD
2. OleOle
3. Morele
-------
##Opis plików
####Config.py
#####zawiera funkcje konfiguracyjne:
- configure_session() - zwraca obiekt Session() z pakietu requests skonfigurowany 
w taki sposób, aby mechanizm utrzymywania połączenia był wyłączony oraz 
w przypadku niepowodzenia z kodem błędu z listy [500, 502, 503, 504] 
dokonano powtórzenia zapytania po wskazanym czasie [0,5 s]
-------

####link_generators/LinkGen.py
Abstrakcyjna klasa podstawowa do obiektów zarządzającymi linkami z produktami w sklepach internetowych. Stanowi szablon do klas pochodnych: MediaExpertLinkGen
#####stałe [zmienne w klasie, które nie mogą być zmieniane]:
- QUERY_STRING_BASE - szablon do URL pod, pod którym znajdują się produkty w sklepie
- SEPARATOR - znak jakim zastępowana jest spacja w danym adresie URL
- PAGE_STRING - łańcuch znaków dodawany do podstawowego linku używany do stronnicowania
- SHOP_NAME = nazwa sklepu
#####zmienne używane w klasach pochodnych:
- product_url - url pod jakim w sklepie znajdują się wyniki wyszukiwania
- query_string - uzupełniony url do zapytania o konkretny produkt na konkretnej stronie
- max_pages - numer ostatniej strony z wynikiem wyszukiwania
#####metody:

