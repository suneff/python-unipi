import datetime, math
import urllib2, sys

i =raw_input("What date are you interested in? (d-m-Y) \t")
dt = datetime.datetime.strptime(i, "%d-%m-%Y")
timestamp=(dt-datetime.datetime(1970,1,1)).total_seconds()
timestamp=str(int(math.floor(timestamp)))


coins=["0","0"]

inp=str(raw_input("Enter two coins that you are interested in learning their value. \n Please seperate them by comma (,). \t")).upper()

coins= inp.split(",")


response=urllib2.urlopen("https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms="+coins[0]+","+coins[1]+"&ts="+timestamp)

html=response.read()
html=html[8:-2]
values=html.split(",")
first=values[0].split(":")
second=values[1].split(":")



if first[1]>second[1]:
    print first[0], first [1], "\n", second[0], second[1]
elif first[1]<second[1]:
    print second[0], second[1], "\n", first[0], first [1]
else :
    print "They both have the same value which is:", second[1]
