import json
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

#--------------------------------------------------
#------------- Práce s JSON katalogem -------------
os.getcwd()
os.chdir(r'\Final Project')

# Načtení souboru json - katalog poboček a produktů
with open(r'Data\catalogue.json', "r", encoding= 'UTF-8') as json_soubor:
    katalog_data = json.load(json_soubor)


# funkce na prozkoumání json souboru:
def verify_json(catalogue):
    potrebne_keys = ['season', 'name_of_shop', 'list_of_branches', 'list_of_products']
    dostupne_keys = list(catalogue.keys())
    print("Ověření úplnosti souboru:")
    if potrebne_keys == dostupne_keys:
        print("- Ano, soubor je úplný \n")
    else:
        print("- Soubor není úplný, nebo obsahuje něco navíc \n")


    # kontrola sezóny:
    print("Je katalog platný pro sezónu 2023/24?")
    if catalogue['season'] == '2023/24':
        print("- Ano, sezóna je správná. Katalog je na sezónu 2023/24")
    else:
        print(f"- Ne, sezóna není správná. Katalog je na sezónu {catalogue['season']} \n")


    # počet poboček:
    print("Kolik má obchod poboček?")
    branches = catalogue['list_of_branches']
    print(f"- Počet poboček: {len(branches)} \n")


    # Kontrola nových poboček:
    print("Bude se otevírat nějaká nová pobočka?")
    datetime.now()    
    new_branch = False
    for branch in branches:
        launch_date = datetime.strptime(branch["Launch_Date"], "%Y-%m-%d")
        if launch_date > datetime.now():
            new_branch = True
            if new_branch:
                if launch_date == "2025-01-01":
                    print(f"- Ano, bude se otevírat nová pobočka ve městě {branch['Location']} \n")
                    print("Bude pobočka otevírat 1. ledna 2025 ?")
                    print(f"- Ano, nová pobočka otevírá dne {launch_date.strftime("%d-%m-%Y")}")
                else:
                    print(f"- Ano, bude se otevírat nová pobočka ve městě {branch['Location']} \n")
                    print("Bude pobočka otevírat 1. ledna 2025 ?")
                    print(f"- Ne, nová pobočka otevírá dne {launch_date.strftime("%d-%m-%Y")}")
    if not new_branch:
        print("- V datech není žádná nová pobočka")

verify_json(katalog_data)

#--------------------------------------------------
#----------------- Práce v Pandas -----------------

with open(r'Data\catalogue.json', "r", encoding= 'UTF-8') as json_soubor:
    katalog_data = json.load(json_soubor)
produkty_df = pd.DataFrame(katalog_data['list_of_products'])

print(f"""
Počet kategorií: {produkty_df['Category'].nunique()} 
Počet produktů: {produkty_df['ID'].nunique()}
Počet značek: {produkty_df['Brand'].nunique()}
    """)

print("Kontrola cen produktů:")
serazeni = produkty_df.sort_values(
    by= ['Catalogue_Price'],
    ascending= True,
    na_position= 'last'
)
nelogicke_ceny = produkty_df[produkty_df['Catalogue_Price'] < 0 ]
produkty_df = produkty_df[produkty_df['Catalogue_Price'] >= 0 ]

print(f"""
ID produktů, které mají chybně uvedenou cenu (zápornou):
{list(nelogicke_ceny['ID'])}
Uvedené produkty byly odstraněny z produkty_df
    """)

# Jaká je průměrná cena všech produktů dohromady?
# Produkty které kategorie jsou nejdražší?
# Produkty které kategorie jsou nejlevnější?
# Která značka má nejvíce produktů v katalogu?

avg_price_all_products = produkty_df['Catalogue_Price'].mean()
avg_price_by_category = produkty_df.groupby('Category')['Catalogue_Price'].mean()
most_expensice_category = avg_price_by_category.idxmax()
the_cheapest_category = avg_price_by_category.idxmin()
brand_product_count = produkty_df.groupby('Brand')['ID'].count()
top_brand = brand_product_count.idxmax()

print(f"""
Průměrná cena všech produktů: {round(avg_price_all_products, 1)} zł
Nejdražší kategorie produktů: {most_expensice_category}
Nejlevnější kategorie produktů: {the_cheapest_category}
Značka s nejvíce produkty: {top_brand}
    """)

# Který produkt této značky je nejdražší a kolik stojí?
# Který produkt této značky je nejlevnější a kolik stojí?
top_brand_df = produkty_df[produkty_df['Brand'] == top_brand]
top_brand_nejdrazsi = top_brand_df.loc[top_brand_df["Catalogue_Price"].idxmax()]
top_brand_nejlevnejsi = top_brand_df.loc[top_brand_df["Catalogue_Price"].idxmin()]

print(f""" 
Nejdražší produkt značky {top_brand}:
{top_brand_nejdrazsi['Model']} ... cena: {top_brand_nejdrazsi['Catalogue_Price']} zł \n 
Nejlevnější produkt značky {top_brand}:
{top_brand_nejlevnejsi['Model']} ... cena: {top_brand_nejlevnejsi['Catalogue_Price']} zł
      """)


#--------------------------------------------------
#--------------------- Grafy ----------------------

# Nastavím si vzhled grafů:
figsize = (8, 4)
plt.rcParams["axes.facecolor"] = "#212121"
plt.rcParams["figure.facecolor"] = "#212121"
plt.rcParams["axes.labelcolor"] = "white"
plt.rcParams["xtick.color"] = "white"
plt.rcParams["ytick.color"] = "white"
plt.rcParams["axes.titlecolor"] = "white"

# Průměrná cena produktů podle značek:
avg_price_by_brand = produkty_df.groupby("Brand")["Catalogue_Price"].mean()
avg_price_by_brand.sort_values().plot(kind="bar", figsize=figsize, color="#60e0ff")
plt.title("Průměrná cena produktů podle značek")
plt.ylabel("Průměrná cena")
plt.xlabel("Značka")
plt.show()
plt.savefig(r"\průměrná_cena_produktů_podle_značek.jpg")

# Průměrná cena produktů podle kategorií:
avg_price_by_category = produkty_df.groupby("Category")["Catalogue_Price"].mean()
avg_price_by_category.sort_values().plot(kind="barh", figsize=figsize, color="#60e0ff")
plt.title("Průměrná cena produktů podle kategorií")
plt.xlabel("Průměrná cena")
plt.ylabel("Kategorie")
plt.show()
plt.savefig(r"\průměrná_cena_produktů_podle_kategorií.jpg")

# Počet produktů podle kategorií:
category_counts = produkty_df["Category"].value_counts()
category_counts.plot(kind="pie", figsize=(6, 6), autopct="%1.1f%%", textprops={"color": "white"})
plt.title("Počet nabízených produktů podle kategorií")
plt.ylabel("")
plt.show()
plt.savefig(r"\počet_produktů_podle_kategorií.jpg")

#--------------------------------------------------
#---------------- Spojení tabulek -----------------

with open(r'Data\catalogue.json', "r", encoding= 'UTF-8') as json_soubor:
    katalog_data = json.load(json_soubor)

branches = pd.DataFrame(katalog_data['list_of_branches'])
products = pd.DataFrame(katalog_data['list_of_products'])
ski_orders_df = pd.read_csv(
    filepath_or_buffer= r"\ski_orders.csv", 
    sep= ',', 
    decimal='.', 
    encoding='UTF-8')

complete_df = pd.merge(
    left= ski_orders_df,
    right= branches[['ID', 'Location', 'Country']],
    how= 'left', 
    left_on= ['Branch_ID'], 
    right_on= ['ID']
)

complete_df = pd.merge(
    left= complete_df,
    right= products,
    how= 'left', 
    left_on= ['Product_ID'], 
    right_on= ['ID']
)

complete_df = complete_df.drop(columns=["ID_x", "ID_y"])


#--------------------------------------------------
#------------------ Webscraping -------------------

service = ChromeService(ChromeDriverManager().install())
browser = Chrome(service=service)

url = "https://www.fis-ski.com/DB/general/results.html?sectorcode=AL&raceid=122772"
browser.get(url)

names = browser.find_elements("class name", "g-lg-10.g-md-10.g-sm-9.g-xs-8.justify-left.bold")
fis_codes = browser.find_elements("class name", "pr-1.g-lg-2.g-md-2.g-sm-2.hidden-xs.justify-right.gray")
birth_years = browser.find_elements("class name", "g-lg-1.g-md-1.hidden-sm-down.justify-left")
countries = browser.find_elements("class name", "country__name-short")

zavodnici_data = []
for name, code, year, country in zip(names, fis_codes, birth_years, countries):
    zavodnici_data.append({
        "Name": name.text,
        "FIS Code": code.text,
        "Birth Year": year.text,
        "Country": country.text
    })
browser.quit()

zavodnici_df = pd.DataFrame(zavodnici_data)
zavodnici_df['FIS Code'] = zavodnici_df['FIS Code'].astype(int)

df = pd.merge(
    left= complete_df,
    right= zavodnici_df[['Name', 'FIS Code', 'Country']],
    how= 'left',
    left_on= ['Racer_ID'],
    right_on= ['FIS Code']
)

df.rename(columns={"Country_x": "Branch_country"}, inplace=True)
df.rename(columns={"Country_y": "Athlete_country"}, inplace=True)
