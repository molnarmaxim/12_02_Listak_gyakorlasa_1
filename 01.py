"""

Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát!
1. Mennyi a sorozatban található számok szorzata?
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
4. Igaz-e, hogy minden szám negatív?
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
6. Hány 18-cal osztható szám található a sorozatban?
7. Mennyi a sorozatban található egyik legkisebb szám indexe?
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?
11. Válogassuk ki két listába a páros és a páratlan számokat!

"""
import random
import json
import time
from datetime import datetime


szamok = [random.randint(-60, 100) for _ in range(50)]

# Műveletek
def szorzat(szamok):
    szorzat = 1
    for szam in szamok:
        szorzat *= szam
    return szorzat

def oszthato_5_vagy_7(szamok):
    for i in range(len(szamok) - 1, -1, -1):
        if szamok[i] % 5 == 0 or szamok[i] % 7 == 0:
            return i
    return None

def oszthato_3_es_7(szamok):
    indexek = []
    for i in range(len(szamok)):
        if szamok[i] % 3 == 0 and szamok[i] % 7 == 0:
            indexek.append(i)
    return indexek

def minden_szam_negativ(szamok):
    for szam in szamok:
        if szam >= 0:
            return "Hamis"
    return "Igen"

def van_szam_1_es_10_kozott(szamok):
    for szam in szamok:
        if 1 <= szam <= 10:
            return "Van"
    return "Nincs"

def hany_szam_oszthato_18_cal(szamok):
    return sum(1 for szam in szamok if szam % 18 == 0)

def legkisebb_szam_indexe(szamok):
    min_szam = szamok[0]
    min_index = 0
    for i in range(1, len(szamok)):
        if szamok[i] < min_szam:
            min_szam = szamok[i]
            min_index = i
    return min_index

def szamok_negyzete_17_vagy_18(szamok):
    negyzetek = []
    for szam in szamok:
        if szam % 17 == 0 or szam % 18 == 0:
            negyzetek.append(szam ** 2)
    return negyzetek

def negativ_szam_szomszedai_positivok(szamok):
    for i in range(1, len(szamok) - 1):
        if szamok[i] < 0 and szamok[i - 1] > 0 and szamok[i + 1] > 0:
            return "Van"
    return "Nincs"

def szigoruan_monoton_novekvo(szamok):
    for i in range(len(szamok) - 1):
        if szamok[i] >= szamok[i + 1]:
            return "Hamis"
    return "Igaz"

def paros_es_paratlan(szamok):
    paros = []
    paratlan = []
    for szam in szamok:
        if szam % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)
    return f"\nParos: {paros}\nParatlan: {paratlan}"

adatok = {
    "datum": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "szamok": szamok,
    "szorzat": szorzat(szamok),
    "oszthato_5_vagy_7_index": oszthato_5_vagy_7(szamok),
    "oszthato_3_es_7_indexek": oszthato_3_es_7(szamok),
    "minden_szam_negativ": minden_szam_negativ(szamok),
    "van_szam_1_es_10_kozott": van_szam_1_es_10_kozott(szamok),
    "hany_szam_oszthato_18_cal": hany_szam_oszthato_18_cal(szamok),
    "legkisebb_szam_indexe": legkisebb_szam_indexe(szamok),
    "negyzetek_17_vagy_18": szamok_negyzete_17_vagy_18(szamok),
    "negativ_szam_szomszedai_positivok": negativ_szam_szomszedai_positivok(szamok),
    "szigoruan_monoton_novekvo": szigoruan_monoton_novekvo(szamok),
    "paros_es_paratlan": paros_es_paratlan(szamok)
}

with open("szamok.json", "w") as f:
    json.dump(adatok, f, indent=4)

print("1. A sorozat szorzata:", adatok["szorzat"])
print("2. Az utolsó 5-tel vagy 7-tel osztható szám indexe:", adatok["oszthato_5_vagy_7_index"])
print("3. Az első 3-mal és 7-tel osztható szám indexei:", adatok["oszthato_3_es_7_indexek"])
print("4. Igaz-e, hogy minden szám negatív?", adatok["minden_szam_negativ"])
print("5. Van-e olyan szám, ami 1 és 10 között van?", adatok["van_szam_1_es_10_kozott"])
print("6. Hány 18-cal osztható szám van?", adatok["hany_szam_oszthato_18_cal"])
print("7. A legkisebb szám indexe:", adatok["legkisebb_szam_indexe"])
print("8. A 17-tel vagy 18-cal osztható számok négyzetei:", adatok["negyzetek_17_vagy_18"])
print("9. Van-e olyan negatív szám, amelynek az összes szomszédja pozitív?", adatok["negativ_szam_szomszedai_positivok"])
print("10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?", adatok["szigoruan_monoton_novekvo"])
print("11. Páros és páratlan számok:", adatok["paros_es_paratlan"])
time.sleep(1)
print("\nMinden adat mentve a 'szamok.json' fájlba! ✅")