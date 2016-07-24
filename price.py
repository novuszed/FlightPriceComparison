__author__ = 'zihaozhu'
import airPort
import airportSym
import csv
import datetime
from datetime import timedelta as td
import time
IATAList = list()
startEndDates=list()
finalDateList = list()
#find all subsets of size 2 between any two given dates in a year
def subset2(dateList, tempList, k, start):
    #print(len(tempList))
    #print(tempList)
    if(len(tempList)==k):
        if(not tempList in finalDateList):
            print(tempList)
            finalDateList.append(tempList[:])
        return
    for i in range(start,len(dateList)):
        tempList.append(dateList[i])
        subset2(dateList,tempList,k,i+1)
        tempList.pop(len(tempList)-1)

    return
#read the csv file and parse for airport codes
def readCSV():

    with open('airportcodes.csv') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        #skip header
        next(file)
        for row in file:
            #print (row[2])
            if(len(row[2])<1):
                IATAList.append(row[2])
#gather all possible dates in datetime in a year frame
def listOfDates():
    d =datetime.datetime.now()
    startd = datetime.date(d.year,d.month,d.day)
    endd=datetime.date(d.year+1,d.month,d.day)
    delta = endd-startd
    for i in range(delta.days+1):
        startEndDates.append(startd+td(days=i))
        #print (startd + td(days=i))
#Finding all prices
def findPrices(dateList, airCodeList):
    for dates in dateList:
        startdate= (dates[0].strftime("%Y-%m-%d"))
        enddate=(dates[1].strftime("%Y-%m-%d"))
        print(startdate, enddate)
        depart=""
        dest=""

        googleFlightLink = "https://www.google.com/flights/#search;f=%s;t=%s;d=%s;r=%s" %(depart,dest,startdate,enddate)

#readCSV()

testdata = list()
testdata.append([datetime.date(2016,10,7),datetime.date(2017,1,13)])
testdata.append([datetime.date(2016,3,7),datetime.date(2017,2,13)])
findPrices(testdata, "test")
#listOfDates()
#subset2(startEndDates,list(),2,0)
#print(finalDateList)