__author__ = 'zihaozhu'
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from socket import timeout
import os
import re
import csv
from string import ascii_lowercase
from airPort import airPort

#write data to csv given airport list
def writeToCsv(airPortList):
    print("-----------Writing to CSV--------------")
    with open('airportcodes.csv', 'w', newline='') as csvfile:
        airCodeWriter = csv.writer(csvfile, delimiter=',',lineterminator='\r\n',quoting=csv.QUOTE_MINIMAL)
        for port in airPortList:
            #takes care of names with unicode characters
            cityName = u''.join(port.getCity()).encode('utf-8').strip()
            countryName=u''.join(port.getCountry()).encode('utf-8').strip()
            airCodeWriter.writerow([cityName,countryName, port.getIATA(), port.getICAO(), port.getFAA()])
#parses the link to find all the air port codes and city names and countries
def htmlParser():
    allAirPorts = list()
    for c in ascii_lowercase:
        airPortCodes = 'https://www.world-airport-codes.com/alphabetical/airport-code/%c.html' %c
        try:
            print("------------Accessing %s --------------" %airPortCodes)
            page = urlopen(airPortCodes)
        except urllib.error.URLError:
            print("User does not exist")
            exit(0)
        except urllib.error.HTTPError:
            print("Something went wrong!")
            exit(0)
        except timeout:
            print("Time out!")
            exit(0)
        soup = bs(page.read(),"html.parser")
        table = soup.find('table', {'class':'responsive'}).find_all('tbody')
        #print(table)
        #print("length: %d "% len(table))
        for airport in table:
            #print ("airport %s" % airport)
            airportData = airport.find_all('tr')
            for port in airportData:
                portData = port.find_all('td')
                count = 0
                rowList = list()
                for row in portData:
                    tempText = row.getText().strip()
                    rowList.append(tempText)
                    #print("Text %s" % tempText)
                    count+=1
                    if(count==5):
                        count = 0
                        currAirPort = airPort(rowList[0],rowList[1],rowList[2],rowList[3],rowList[4])
                        allAirPorts.append(currAirPort)
                        rowList.clear()

    #print(allAirPorts)
    writeToCsv(allAirPorts)
#htmlParser()