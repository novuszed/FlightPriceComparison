__author__ = 'zihaozhu'
import airPort
import airportSym
import csv
import datetime
import urllib
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import operator
from socket import timeout
import os
import re
from datetime import timedelta as td
import time
import networkx as nx




IATAList = list()
finalIATAList=list()
startEndDates=list()
finalDateList = list()
#find all subsets of size 2 between any two given dates in a year
def subset2(dateList, tempList, k, start):
    if(len(tempList)==k):
        if(not tempList in finalDateList):
            finalDateList.append(tempList[:])
        return
    for i in range(start,len(dateList)):
        tempList.append(dateList[i])
        subset2(dateList,tempList,k,i+1)
        tempList.pop(len(tempList)-1)

    return

def airCodesubset2(dateList, tempList, k, start):
    if(len(tempList)==k):
        if(not tempList in finalIATAList):
            finalIATAList.append(tempList[:])
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
            if(len(row[2])>0):
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
        for aircode in airCodeList:
            depart=aircode[0]
            dest=aircode[1]
            print("------------Departure Airport %s %s------ \n"
                  "------------Arrival Airport %s %s-------" %(depart,startdate,dest,enddate))
            FlightLink ='https://www.kayak.com/flights/%s-%s/%s/%s' %(depart,dest,startdate,enddate)
            parseHtml(FlightLink,startdate,enddate)
def parseHtml(link,startdate,enddate):
    try:
        print("------------Accessing %s --------------" %link)
        page = urlopen(Request(link,headers={'User-Agent': 'Chrome/35.0.1916.47'}))
    except urllib.error.URLError:
        print("User does not exist")
        exit(0)
    except urllib.error.HTTPError:
        print("Something went wrong!")
        exit(0)
    except timeout:
        print("Time out!")
        exit(0)
    prices = list()
    data = dict()
    soup = bs(page.read(),"html.parser")
    #match any unique ID
    counter = 0
    infoLink = re.compile('infolink\d+')
    div = soup.find_all('div',{'id':infoLink})
    for id in div:
        if(counter==3):
            break
        counter+=1
        price = id.find('div', {'class':'mainInfoDiv'})
        price = price.getText().split()
        prices.append(price[0])
        data["%s->%s"%(startdate,enddate)] = prices
    print(prices)
    print(data)
    return data
    #print(len(div))
    #print(div)
#finds the lowest price given a set interval period of time
def getLowestPrice(depart, arrival, dateList,lenDays):
    for dates in dateList:
            startdate= (dates[0].strftime("%Y-%m-%d"))
            enddate=(dates[1].strftime("%Y-%m-%d"))
            if(enddate-startdate != lenDays):
                continue
            depart=depart
            dest=arrival[1]
            print("------------Departure Airport %s %s------ \n"
                  "------------Arrival Airport %s %s-------" %(depart,startdate,dest,enddate))
            FlightLink ='https://www.kayak.com/flights/%s-%s/%s/%s' %(depart,dest,startdate,enddate)
            parseHtml(FlightLink,startdate,enddate)

#sort by the cheapest flight and return
def getCheapest(data):
    sorted_data= sorted(data.items(), key=operator.itemgetter(1)[0])
    return sorted_data

def userPrompt():
    startDate = input("Please enter starting date in format YYYY-MM-DD")
    endDate = input("Please enter ending date in format YYYY-MM-DD")
    departure = input("Input 3 letter IATA codes for the airport. Refer to the CSV for information")
    arrival = input("Input 3 letter IATA codes for the airport. Refer to the CSV for info")
    getLowestPrice(departure,arrival,list([startDate,endDate]),endDate-startDate)
    


#readCSV()
#print(IATAList)
#airCodesubset2(IATAList,list(),2,0)
testdata = list()
testdata.append([datetime.date(2016,10,7),datetime.date(2017,1,13)])
testdata.append([datetime.date(2016,8,7),datetime.date(2017,2,13)])
testair = list()
testair.append(["AUS","JFK"])

findPrices(testdata, testair)
#listOfDates()
#subset2(startEndDates,list(),2,0)
#print(finalDateList)