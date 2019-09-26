from bs4 import BeautifulSoup
import requests
import json

r = requests.get("http://digidb.io/digimon-list/")
soup = BeautifulSoup(r.content,'html.parser')

dataTarget = soup.find_all('tr')

# print(dataTarget[0:])
dataDigiomon = []

for i in dataTarget[1:]:
        nomor = (i.b.text)
        nama = (i.a.text)
        image = (i.img['src'])
        stage = (i.center.text)
        typee = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().text)
        attribute = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        memory = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        equip_slot = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        hp =(i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        sp = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        atk = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        deff = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        intt = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
        spd = (i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)

        data = {
            'no': int(nomor),
            'digimon': nama,
            'image': image,
            'stage':stage,
            'type':typee,
            'attribute':attribute,
            'memory':memory,
            'equip slots': equip_slot,
            'hp':hp,
            'sp':sp,
            'atk':atk,
            'def':deff,
            'int':intt,
            'spd':spd 
            }
        
        dataDigiomon.append(data)

with open('digimon.json','w') as x :
    x.write(str(dataDigiomon).replace("'",'"'))






