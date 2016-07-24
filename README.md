# FlightPriceComparison

Script that parses a list of airport IATA codes and stores it in a CSV with the city name, country name, FAA code and ICAO codes. 
This creates a tiny data base that helps facilitate queries as needed. 
It allows users to input a departure airport and an arrival airport with a period of time they would like to stay and get back, and
the script then finds the lowest price for the airplane ticket and returns the period of time in which users should take the trip.

Other functionality including aggregating data for all airports to all other airports in a span of one year (this creates millions of data so
it's best to not use unless given permission to crawl a website that much). 
