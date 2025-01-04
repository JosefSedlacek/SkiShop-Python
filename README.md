# SkiShop-Python
Python projekt z kurzu od CodersLab

# Zadání:

## Část 1 - Ověření katalogu

Jedná se o data obchodu One&Only Ski Shop. Je to známý prodejce, který 
nabízí široký sortiment produktů pro vášnivé lyžaře. Tento obchod dodával vybavení i všem závodníkům, kteří se zúčastnili závodů Světového poháru v alpském lyžování v disciplíně super-G, včetně Jana Zabystřana.

Poslali nám katalog ve formátu JSON. Zkontroluj následující:
* Ověř verzi katalogu – je to opravdu sezóna 2023/24?
* Kolik poboček mají? Měli by mít tři pobočky v Evropě.
* Plánují otevření nové pobočky, ta v datech ale asi ještě nebude. Pokud tam nějaká bude, zkontroluj, zda bude otevřena 1.1.2025.
* Vypiš kontakty na všechny manažery včetně jejich jmen
* Budou postupně posílat další katalogy ve stejném formátu, proto na tuto kontrolu vytvoř funkci "verify_json".


## Část 2 - Analýza produktů z katalogu

Zpracujte část list_of_products - uložte si ji jako samostatný dataframe (knihovna Pandas). Odpovězte na následující otázky:
* Kolik kategorií produktů nabízí One&Only Ski Shop?
* Kolik celkově produktů se nachází v katalogu?
* Kolik značek má v nabídce One&Only Ski Shop?
* Zkontrolujte, zda se v datech nenacházejí nelogické hodnoty - zaměřte se na cenu
	* Pokud ano, zapište si ID produktů a odstraňte je z katalogu (JSON nemusíte ukládat)
* Jaká je průměrná cena všech produktů dohromady?
* Produkty které kategorie jsou nejdražší?
* Produkty které kategorie jsou nejlevnější?
* Která značka má nejvíce produktů v katalogu?
	* Který produkt této značky je nejdražší a kolik stojí?
	* Který produkt této značky je nejlevnější a kolik stojí?
* Pomocí grafů (matplotlib) zobrazte následující:
	* Průměrnou cenu produktů podle jednotlivých značek.
		* Sloupcový diagram
	* Průměrnou cenu produktů podle kategorií produktů.
		* Sloupcový (horizontální) diagram
	* Počet nabízených produktů podle kategorií.
		* Koláčový graf 

## Část 3 - Webscraping

Podařilo se nám zjistit, co za závodníky tam je. Všichni závodníci z tabulky jeli závod Světového poháru 7.12.2024, v Beaver Creeku v USA. Vyhrál ho tehdy Marco Odermatt ze Švýcarska. Výsledky závodu jsou k dispozici na této stránce:

https://www.fis-ski.com/DB/general/results.html?sectorcode=AL&raceid=122772

Kromě toho jsou tam jména všech závodníků se svým ID (FIS Code), rokem narození, zemí, kterou reprezentují, a výsledným časem, či počtem získaných bodů. Prosím, doplňte údaje o závodnících a objednaných produktech do tabulky objednávek.

#### Úkoly:
Načtěte si pomocí Pandas soubor ski_orders.csv. V souboru se nachází sloupec Branch_ID - použijte data z katalogu a přidejte tam údaje o pobočce (nemusíte přidávat jméno manažera a telefonní číslo). Nezapomeňte, nechcete přijít o žádnou položku z tabulky ski_orders. V souboru se nachází sloupec Product_ID - použijte data z katalogu a přidejte tam údaje o produktu. Nezapomeňte, nechcete přijít o žádnou položku z tabulky ski_orders. Seznam závodníků si musíte vytvořit vy. Použijte výše uvedený odkaz a pomocí knihovny Selenium získejte následovné informace o závodnících:
* Jméno a příjmení
* FIS Code
* Rok narození
* Země, kterou reprezentují  
* Spočítejte sloupec total_value - má jít o vynásobený počet objednaných produktů a cenu jednotlivých produktů (pro každou položku zvlášť). 

Zkontrolujte následující chyby:
* Některé produkty, které jste z katalogu odstranili, nyní mohou chybět. Kolik takových položek se nachází v tabulce? Kolik celkově bylo takto objednaných produktů?
* Některé položky jsou objednávky v budoucnosti - to nevadí. Avšak problém je, pokud byla objednávka vytvořena na ještě neotevřené pobočce. Ověřte, zda se tam nacházejí 
takové objednávky. Jaká je jejich celková hodnota? Pomocí .loc přiřaďte tyto objednávky do pobočky v Curychu.  

Odpovězte na následující otázky:
* Kolik objednávek (počet unikátních Order_ID) vytvořil HROBAT Miha?
* Za jakou sumu celkově vytvořil objednávky MONSEN Felix?
* Který závodník vytvořil nejdražší objednávku (součet celkové hodnoty total_value podle Order_ID)?
* Závodníci, z které země objednali nejvíce kusů produktů?
* Jaké produkty si objednal ZABYSTRAN Jan? Kolik za ně celkově zaplatil?
* Který závodník udělal úplně první objednávku - podle data?
* Která pobočka je nejúspěšnější? Zhodnoťte to podle více parametrů:
	* Počet prodaných kusů.
	* Počet unikátních objednávek.
	* Celková hodnota objednávek.
* Který produkt se nejlépe prodává?

Pomocí pomocných sloupců odpovězte na tyto otázky:
* Ve kterých třech měsících byla nejvyšší hodnota objednávek (pomocný sloupec month)?
* Jak se měnila celková hodnota objednávek v jednotlivých rocích (pomocný sloupec year)
