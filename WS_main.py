
import requests
import xlrd
import pandas
from  bs4 import BeautifulSoup
'''
py -3 WS_main.py
'''
#r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
r    = requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c    = r.content
soup = BeautifulSoup(c,"html.parser")
all_Bed1  = ''
all_SQft1 = 0
all_Bath  = 0
all_VHB  = 0
l = []
#print(soup)
all_DIV_pr = soup.find_all("div",{"class":"propertyRow"}) # per riconoscere solo i div con  identificativo cities
#    all_H4_pr = all_DIV_pr[0].find("h4",{"class":"propPrice"}).text.replace("\n", "").replace(" ","") # per riconoscere solo i div con  identificativo cities



for i in all_DIV_pr:
    d={}
    d["PRICE"   ]     = i.find("h4",{"class":"propPrice"}).text.replace("\n", "").replace(" ","")
    d["ADDRESS" ]     = i.find_all("span",{"class":"propAddressCollapse"})[0].text
    d["LOCALITY"]     = i.find_all("span",{"class":"propAddressCollapse"})[1].text
    try:
        d["SQR_FT"]  = i.find("span",{"class":"infoSqFt"}).find("b").text
    except:
        d["SQR_FT"]  =None
    try:
        d["BEDS"]  = i.find("span",{"class":"infoBed"}).find("b").text
    except:
        d["BEDS"]  = None
    try:
        d["BATHS"]  = i.find("span",{"class":"infoBath"}).find("b").text
    except:
        d["BATHS"]  = None
    try:
        d["VALUE_H_B"] = i.find("span",{"class":"infoValueHalfBath"}).find("b").text
    except:
        d["VALUE_H_B"] = None

    for columnGroup in i.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(columnGroup.find_all("span",{"class":"feature_group"}) , columnGroup.find_all("span",{"class":"feature_name"}) ): #per iteradata in 2 liste contemporaneamente
             #print(feature_group.text,feature_name.text)
             if "Lot size" in feature_group.text:
                 d["LOT_SIZE"] = feature_name.text
                 #print("CERCATO : " + str(feature_group.text))
    l.append(d)
  #Data_Frame
    #print(all_H4_pr)
    #print(all_H4_address_0)
    #print(all_H4_address_1)
    #print(all_SQft1)
    #print("Bed               :" + str(all_Bed1))
    #print("N Baths           :" + str(all_Bath))
    #print("infoValueHalfBath :" + str(all_VHB ))

df = pandas.DataFrame(l)
df.to_csv("new_PROPERTY_FILE.csv") #scrvo Dataframe su file
