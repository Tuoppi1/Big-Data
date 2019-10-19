import sys
import requests
import csv
import time


fileName = sys.argv[1]
timeInterval = int(sys.argv[2])
recordTime = float(sys.argv[3])

def collectBussData(fileName,rawBusData):
    allBusses = rawBusData["body"]
    with open(fileName,"a") as bussDataCSV:
        writer = csv.writer(bussDataCSV,delimiter =";")
        dataList = []
        for i in range(0,len(allBusses)):
            allData = []
            busData = rawBusData["body"][i]
            allData.append("Date: {}".format(busData["monitoredVehicleJourney"]["framedVehicleJourneyRef"]["dateFrameRef"]))
            recordedStringTime = (str(busData["recordedAtTime"][11:]))[:-10]
            allData.append("Time: {}".format(recordedStringTime))
            allData.append("Line: {}".format(busData["monitoredVehicleJourney"]["lineRef"]))
            allData.append("Vehilce: {}".format(busData["monitoredVehicleJourney"]["vehicleRef"]))
            allData.append("Direction: {}".format(busData["monitoredVehicleJourney"]["directionRef"]))
            allData.append("latitude: {}".format(busData["monitoredVehicleJourney"]["vehicleLocation"]["latitude"]))
            allData.append("Longitude: {}".format(busData["monitoredVehicleJourney"]["vehicleLocation"]["longitude"]))
            allData.append("Speed: {}".format(busData["monitoredVehicleJourney"]["speed"]))
            dataList.append(allData)
            writer.writerow(dataList[i])
        
start = time.time()
while True:
    rawBusData = requests.get("http://data.itsfactory.fi/journeys/api/1/vehicle-activity").json()
    collectBussData(fileName,rawBusData)
    end = time.time()
    if (end - start) > recordTime:
        break
    time.sleep(timeInterval)
print("Buss data has been collected successfully!")
