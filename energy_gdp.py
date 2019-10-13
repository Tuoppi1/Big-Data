from urllib.request import urlopen
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt

with urlopen("http://api.worldbank.org/countries/fin/indicators/EG.USE.PCAP.KG.OE") as link1,\
urlopen("http://api.worldbank.org/countries/fin/indicators/EG.USE.PCAP.KG.OE?page=2") as link2,\
urlopen("http://api.worldbank.org/countries/fin/indicators/NY.GDP.PCAP.CD") as link3,\
urlopen("http://api.worldbank.org/countries/fin/indicators/NY.GDP.PCAP.CD?page=2") as link4:
    energyData = et.parse(link1)
    energyData2 = et.parse(link2)
    gdpData = et.parse(link3)
    gdpData2 = et.parse(link4)
    
root1 = energyData.getroot()
root2 = energyData2.getroot()
root3 = gdpData.getroot()
root4 = gdpData2.getroot()


energyList = []
gdpList = []

for i in root1:
    dicti = {}
    for e in i:
        if e.tag == "{http://www.worldbank.org}date":
            dicti["date"] = e.text
        if e.tag == "{http://www.worldbank.org}value":
            if e.text == None:
                dicti["value"] = "0"
            else:
                dicti["value"] = e.text
        energyList.append(dicti)
        
for i in root2:
    dicti = {}
    for e in i:
        if e.tag == "{http://www.worldbank.org}date":
            dicti["date"] = e.text
        if e.tag == "{http://www.worldbank.org}value":
            if e.text == None:
                dicti["value"] = "0"
            else:
                dicti["value"] = e.text
        energyList.append(dicti)
        
for i in root3:
    dicti = {}
    for e in i:
        if e.tag == "{http://www.worldbank.org}date":
            dicti["date"] = e.text
        if e.tag == "{http://www.worldbank.org}value":
            dicti["value"] = e.text
        gdpList.append(dicti)
        
for i in root4:
    dicti = {}
    for e in i:
        if e.tag == "{http://www.worldbank.org}date":
            dicti["date"] = e.text
        if e.tag == "{http://www.worldbank.org}value":
            dicti["value"] = e.text
        gdpList.append(dicti)
        
energyList = sorted(energyList,key=lambda x: x["date"])
gdpList = sorted(gdpList,key=lambda x: x["date"])

vuodet = []
energia = []
for i in energyList:
    vuodet.append(int(i["date"]))
    energia.append(float(i["value"]))

vuodet2 = []
gdp = []
for i in gdpList:
    vuodet2.append(int(i["date"]))
    gdp.append(float(i["value"]))

fig, ax1 = plt.subplots()

color = "tab:blue"
ax1.set_xlabel("Year")
ax1.set_ylabel("Energy",color=color)
ax1.plot(vuodet,energia,color=color)
ax1.tick_params(axis="y",labelcolor=color)

ax2 = ax1.twinx()
color = "tab:red"
ax2.set_ylabel("GDP",color=color)
ax2.plot(vuodet2,gdp,color=color)
ax2.tick_params(axis="y",labelcolor=color)

fig.tight_layout()
plt.savefig("energy_vs_gdp.pdf")
