# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

fichier = "devoir3.csv"

# Mon but est de voir les villes d'origine et les destinations des vols que la compagnie Air Transat considère comme étant "pas chers". 
url = "https://www.airtransat.com/fr-CA/vols-pas-chers-du-canada?ici=footerlink&icn=cheap-flights_french"

entetes = {
    "User-Agent":"Éloi Fournier, étudiant en journalisme à l'UQAM"
}

site = requests.get(url, headers=entetes)

page = BeautifulSoup(site.text, "html.parser")
# print(page)

n = 0

# Cette fonction me permet d'obtenir tous les vols pas chers d'Air Transat par pays de destination. 
vols = page.find_all("li", class_="CMSSiteMapListItem")
print(site.status_code)
# print(vols)

# Ma boucle, qui me permettra d'extraire les données que je recherche pour le csv.
for vol in vols: 
    infos=[]
    n += 1
    urlVol = vol.find("a")["href"]
    nomVol = (" ") + vol.find("a").text.strip()
    # print(n, urlVol)
    if "https" in urlVol: 
        print(n, urlVol)
    else: 
        urlVol2 = " https://www.airtransat.com" + str(urlVol)
        print(n, urlVol2)
    print(nomVol)
    infos.append(n)
    infos.append(urlVol2)
    infos.append(nomVol)

    # Code menant à la création de mon csv.
    air = open(fichier,"a")
    transat = csv.writer(air)
    transat.writerow(infos)