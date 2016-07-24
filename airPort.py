__author__ = 'zihaozhu'
class airPort:
    city = ""
    country =""
    IATA = ""
    ICAO = ""
    FAA = ""
    def __init__(self,city,country,iata,icao,faa):
        self.city = city
        self.country = country
        self.IATA = iata
        self.ICAO = icao
        self.FAA = faa
    def setCity(self, city):
        self.city = city
    def setCountry(self, country):
        self.country = country
    def setIATA(self,iata):
        self.IATA = iata
    def setICAO(self,icao):
        self.ICAO = icao
    def setFAA(self,faa):
        self.FAA = faa
    def getCity(self):
        return self.city
    def getCountry(self):
        return self.country
    def getIATA(self):
        return self.IATA
    def getICAO(self):
        return self.ICAO
    def getFAA(self):
        return self.FAA
