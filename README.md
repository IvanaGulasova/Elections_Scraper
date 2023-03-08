### O PROJEKTE
Výsledkom projektu bolo extrahovať data z parlamentných volieb, ktorých adresu prikladám: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103

### POUŽITÉ KNIHOVNE  
Knihovne dôležité pre beh kódu sú uložené v súbore **requirements.txt**. Je potrebné ich vopred inštalovať - doporučuje sa v novom virtuálnom prostredí. Inštalujú sa následovne:  

```
$ pip3 -- version  
$ pip3 install -r requirements.txt
```

### SPUSTENIE PROJEKTU
Pre spustenie programu je dôležité vložiť do príkazového riadku tri argumenty:
- názov súboru
- url adresu konkrétneho okresu
- názov súboru pre vytvorenie csv súboru 

```
 python election-scraper.py <odkaz_územného_celku> <výsledný_csv_súbor> 
```

Výsledkom bude nový csv súbor s výsledkami dát.

### UKÁŽKA PROGRAMU
**Výsledky pre okres Prostějov:**  
  
**1. argument** "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"  
**2. argument** vysledky_prostejov.csv  
```
python election-scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
```

**Priebeh sťahovania dát**
```
STAHUJEM DATA Z VYBRANEHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
UKLADAM DO SUBORU: vysledky.csv ..  
UKONCUJEM elections_scraper  
```

**Čiastočný výstup**
```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
...
```
