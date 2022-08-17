#!/usr/bin/env python3
"""Reading in stocks data"""

# every five minutes, send a GET request to the api
# check if high is above 34,
   # if so, send alert
# check if low is below 29
   # if so, send alert

import time
import requests

uberhigh= 34
uberlow= 30

applehigh= 50
applelow= 40

# put everything below this line in a while loop
uberurl= "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=UBER&interval=5min&apikey=6B1O04N7UW4537IP"

appleurl= "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=6B1O04N7UW4537IP"


# start while loop here

# send a request to UBER first
data= requests.get(uberurl).json()

# check uber prices
for x in data["Time Series (5min)"]:
    # x = key value (2022-08-12 20:00:00)
    currenthigh= data["Time Series (5min)"][x]["2. high"]
    currentlow= data["Time Series (5min)"][x]["3. low"]
    break

# take action
if float(currenthigh) >= uberhigh:
    print("SELL SELL SELL")
elif float(currentlow) < uberlow:
    print("BUY BUY BUY")

# repeat the above, but for apple

# have code wait for 5 minutes

