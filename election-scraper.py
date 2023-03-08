"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Ivana Gulasova
email: ivana.gulasova3@gmail.com
discord: IvanaG#9103
"""

import sys
from requests import get
from bs4 import BeautifulSoup as bs
import csv

def main():
    if len(sys.argv) != 3:
        print("Zadaj tri argumenty!")
        quit()
    
    adresa, nazov_css = sys.argv[1], sys.argv[2]
    print(f"STAHUJEM DATA Z VYBRANEHO URL: {adresa}")

    url = get(adresa)
    soup = bs(url.text, features="html.parser")
    blok = soup.find_all("div", {"class": "t3"})

    tabulka_1 = blok[0].find("table", {"class": "table"})
    riadky_1 = tabulka_1.find_all("tr")    

    tabulka_2 = blok[1].find("table", {"class": "table"})
    riadky_2 = tabulka_2.find_all("tr")
  
    tabulka_3 = blok[2].find("table", {"class": "table"})
    riadky_3 = tabulka_3.find_all("tr")   
                 
    kody,obce = [], [] 

    for riadok in range(2, len(riadky_1)):
        data_na_riadkoch1 = riadky_1[riadok].find_all("td") 
        kody.append(data_na_riadkoch1[0].text)
        obce.append(data_na_riadkoch1[1].text)

    for riadok in range(2, len(riadky_2)):
        data_na_riadkoch2 = riadky_2[riadok].find_all("td") 
        kody.append(data_na_riadkoch2[0].text)
        obce.append(data_na_riadkoch2[1].text)

    for riadok in range(2, len(riadky_3)):
        data_na_riadkoch3 = riadky_3[riadok].find_all("td")
        if data_na_riadkoch3[0].text == '-':
            continue 
        kody.append(data_na_riadkoch3[0].text)
        if data_na_riadkoch3[1].text == '-':
            continue
        obce.append(data_na_riadkoch3[1].text)
    
    okrsky = vsetky_okrsky(tabulka_1, tabulka_2, tabulka_3)
    vsetky_url = vsetky_urls(adresa, okrsky)
    vysledky = data(kody, obce, vsetky_url)
    zapis(nazov_css,vysledky)
    print(f"UKLADAM DO SUBORU: {nazov_css} ..")
    print("UKONCUJEM elections_scraper")


def vsetky_okrsky(tabulka_1, tabulka_2, tabulka_3):
    okrsky = []
    vsetky_tabulky = (tabulka_1, tabulka_2, tabulka_3)
    
    for tabulka in vsetky_tabulky:
        td_tags = (tabulka).find_all("td", {"class": "cislo"})
        for td_tag in td_tags:
            a_tag = td_tag.find("a")    
            if a_tag:
                href = a_tag.get("href")
                okrsky.append(href)
    return okrsky


def vsetky_urls(adresa, okrsky):
    zaciatok = adresa.rsplit("/", 1)[0]
    vsetky_url_okrskov = []

    for okrsok in okrsky:
        nova_url = zaciatok + "/" + okrsok   
        vsetky_url_okrskov.append(nova_url)   
    return vsetky_url_okrskov 


def data( kody, obce, vsetky_url_okrskov):
    zoznam_vysledkov = []

    cislo = 0
    for url in vsetky_url_okrskov:
        url_obce = url
        url_obce = get(url_obce)

        soup2 = bs(url_obce.text, features="html.parser")
        tabulka_mini = soup2.find("table", {"class": "table"})
        riadky_t_m = tabulka_mini.find_all("tr")

        volici = riadky_t_m[2].find("td", {"headers": "sa2"}, {"data-rel": "L1"}).text
        obalky = riadky_t_m[2].find("td", {"headers": "sa3"}, {"data-rel": "L1"}).text
        platne_hlasy = riadky_t_m[2].find("td", {"headers": "sa6"}, {"data-rel": "L1"}).text
        
        blok_2 = soup2.find_all("div", {"class": "t2_470"})
        tab_1 = blok_2[0].find("table", {"class": "table"})
        ria1 = tab_1.find_all("tr")
        
        vysledok = {
                "code": kody[cislo],
                "location": obce[cislo],
                "registered": volici,
                "envelopes": obalky,
                "valid": platne_hlasy
        }
        
        for poradie in range(2,15):
            strana = ria1[poradie].find("td", {"class" :"overflow_name"}).text
            hlasy = ria1[poradie].find("td", {"headers": "t1sa2 t1sb3"}).text
            vysledok[strana] = hlasy

        tab_1 = blok_2[1].find("table", {"class": "table"})
        ria1 = tab_1.find_all("tr")

        for poradie2 in range(2,14):
            strana2 = ria1[poradie2].find("td", {"class" :"overflow_name"}).text
            hlasy2 = ria1[poradie2].find("td", {"headers": "t2sa2 t2sb3"}).text
            vysledok[strana2] = hlasy2

        zoznam_vysledkov.append(vysledok)
        cislo += 1
    return zoznam_vysledkov


def zapis(nazov_sub,data):
    with open(nazov_sub, "w", newline="", encoding="utf-8") as sub_csv:
        hlava = data[0].keys()
        zapis = csv.DictWriter(sub_csv, fieldnames=hlava)
        zapis.writeheader()
        zapis.writerows(data)

if __name__=="__main__":
    main()