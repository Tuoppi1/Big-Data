import re
import time
import requests
import matplotlib.pyplot as plt

# This program uses a russian proxy IP address
# Because i got banned from  www.iplocate.io
# Current proxy worked for me at least
# Use your default IP address by removing proxies parameter from requests.get(url,proxies).json() (line 30)


file = open("logins.txt")
hackList = []
ipAddressList = []
countryDict = {}
proxies = {"https":"195.239.86.102:45871"}
hackTimeDict = {"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,\
                "09":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,\
                "18":0,"19":0,"20":0,"21":0,"22":0,"23":0}
countryList = []

for line in file:
    if "Tue Oct  2" in line:
        ipAddress = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line).group()
        hackTime = re.search("\d+:\d+",line).group()
        
        if ipAddress not in ipAddressList:
            ipAddressList.append(ipAddress)
            
            time.sleep(1)
            hacker = requests.get("https://www.iplocate.io/api/lookup/{}".format(ipAddress)).json()
            hackList.append(hacker)
            try:
                #print(hacker["country"])
                if hacker["country"] in countryDict:
                    countryDict[hacker["country"]] += 1
                else:
                    countryDict[hacker["country"]] = 1
                hackTimeDict[hackTime[:-3]] += 1
            except:
                pass
    #if len(hackList) > 15: # <-- uncomment this and break for testing purposes
        #break

countryList = sorted(countryDict.items(),key=lambda x: x[1],reverse=True)
n = []
label = []
for i in countryList:
    if len(n) == 10:
        break
    n.append(i[1])
    label.append(i[0])

sortedHackTimeList = sorted(hackTimeDict.items(),key=lambda x: x[0])
n1 = []
label1 = []
for i in sortedHackTimeList:
    n1.append(i[1])
    label1.append(i[0])

plt.figure(figsize=(5,5))
plt.figure(1)
plt.pie(n,labels = label)
plt.savefig("hackpie.png")
plt.figure(2)
plt.figure(figsize=(10,6))
plt.bar(label1,n1)
plt.savefig("hackbar.png")
plt.show
