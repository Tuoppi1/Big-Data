import matplotlib.pyplot as plt
import csv

labels = []
makeIndex = 0
kmIndex = 0
ageIndex = 0
co2Index = 0
vehicleTypeIndex = 0

allBrands = {}
kmDict = {"0-50 000 km":0,"50 000-100 000 km":0,"100 000-150 000 km":0,\
          "150 000-200000 km":0,"200 000-250 000 km":0,"250 000-300 000 km":0,\
          "more than 300000 km":0}
allAges = {"5 years old or less":0,"6-10 years old":0,"11-15 years old":0,\
          "16-20 years old":0,"more than 20 years old":0}
co2Dict = {"less than 100g/km":0,"101-125g/km":0,"126-150g/km":0,\
           "151-175g/km":0,"176-200g/km":0,"201-225g/km":0,"226-250g/km":0,\
           "more than 250g/km":0,}


with open("Ajoneuvojen avoin data 5.3.csv","r",encoding="utf8",errors="ignore") as ajoneuvoData:
    reader = csv.reader(ajoneuvoData)
    for line in reader: # Geting the column labels
        labels = line[0].split(";")
        break

    for i in range(0,len(labels)): # retrieving the column indexes from label list
        if labels[i] == "merkkiSelvakielinen":
            makeIndex = i
        if labels[i] == "matkamittarilukema":
            kmIndex = i
        if labels[i] == "ensirekisterointipvm":
            ageIndex = i
        if labels[i] == "Co2":
            co2Index = i
        if labels[i] ==  "ajoneuvoluokka":
            vehicleTypeIndex = i
    testNumber = 0
    for line in reader: # Starting from index 1. Where car data starts from
        testNumber += 1
        carDict = {}
        carStats = line[0].split(";")
        try:
            if carStats[vehicleTypeIndex] == "M1" or carStats[vehicleTypeIndex] == "M1G":
                carDict["Make"] = carStats[makeIndex]
                carDict["km"] = carStats[kmIndex]
                carDict["Date"] = carStats[ageIndex]
                carDict["Co2"] = carStats[co2Index]
                
                if carDict["Make"] in allBrands:
                    allBrands[carDict["Make"]] += 1
                else:
                    allBrands[carDict["Make"]] = 1
                    
                if float(carDict["km"]) <= 50000:
                    kmDict["0-50 000 km"] += 1
                if float(carDict["km"]) <= 100000:
                    kmDict["50 000-100 000 km"] += 1
                if float(carDict["km"]) <= 150000:
                    kmDict["100 000-150 000 km"] += 1
                if float(carDict["km"]) <= 200000 :
                    kmDict["150 000-200000 km"] += 1
                if float(carDict["km"]) <= 250000:
                    kmDict["200 000-250 000 km"] += 1
                if float(carDict["km"]) <= 300000:
                    kmDict["250 000-300 000 km"] += 1
                if float(carDict["km"]) > 300000:
                     kmDict["more than 300000 km"] += 1
                
                if (2018 - int(carDict["Date"][:-6])) <= 5:
                    allAges["5 years old or less"] += 1
                if (2018 - int(carDict["Date"][:-6])) <= 10:
                    allAges["6-10 years old"] += 1
                if (2018 - int(carDict["Date"][:-6])) <= 15:
                    allAges["11-15 years old"] += 1
                if (2018 - int(carDict["Date"][:-6])) <= 20:
                    allAges["16-20 years old"] += 1
                if (2018 - int(carDict["Date"][:-6])) > 20:
                    allAges["more than 20 years old"] += 1
                
                if float(carDict["Co2"]) <= 100:
                    co2Dict["less than 100g/km"] += 1
                if float(carDict["Co2"]) <= 125:
                    co2Dict["101-125g/km"] += 1
                if float(carDict["Co2"]) <= 150:
                    co2Dict["126-150g/km"] += 1
                if float(carDict["Co2"]) <= 175:
                    co2Dict["151-175g/km"] += 1
                if float(carDict["Co2"]) <= 200:
                    co2Dict["176-200g/km"] += 1
                if float(carDict["Co2"]) <= 225:
                    co2Dict["201-225g/km"] += 1
                if float(carDict["Co2"]) <= 250:
                    co2Dict["226-250"] += 1
                if float(carDict["Co2"]) > 250:
                    co2Dict["more than 250g/km"] += 1
        except:
            pass
        #if testNumber > 10000: break #<-- uncomment for testing purposes

sortedAllBrands = sorted(allBrands.items(),key=lambda x: x[1],reverse=True)
brandShare = []
brandLabel = []
for i in sortedAllBrands:
    brandShare.append(i[1])
    brandLabel.append(i[0])
    
top5Brands = brandShare[:5]
brandSum = sum(brandShare[5:])
top5Brands.append(brandSum)

top5Labels = brandLabel[:5]
top5Labels.append("Others")
    
plt.figure(1)
plt.title("Shares of most common car brands in Finland")
f1 = plt.pie(top5Brands)
plt.legend(f1[0],top5Labels)
plt.savefig("vehstats1.png")


plt.figure(2)
plt.title("Shares of car km in Finland")
kmList = kmDict.items()
km1,km2 = zip(*kmList)
f2 = plt.pie(km2)
plt.legend(f2[0],km1,loc="best")
plt.savefig("vehstats2.png")

plt.figure(3)
plt.title("Share of car ages in Finland")
ageList=allAges.items()
age1,age2 = zip(*ageList)
f3 = plt.pie(age2)
plt.legend(f3[0],age1,loc="best")
plt.savefig("vehstats3.png")

plt.figure(4)
plt.title("Share of car Co2 emissions in Finland")
co2List=co2Dict.items()
co1,co2 = zip(*co2List)
f4 = plt.pie(co2)
plt.legend(f4[0],co1,loc="best")
plt.savefig("vehstats4.png")

plt.show
