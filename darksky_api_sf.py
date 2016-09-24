"""
# 2) By using: https://darksky.net/dev/docs
# API KEY: 61982b282ad0e8410101fb450a15edfc
# Display those data:
# - current temperature and summary in San Francisco
# - temperature and summary in San Francisco the 09/24
# - average temparture of the next 8 days in SF

# https://api.darksky.net/forecast/61982b282ad0e8410101fb450a15edfc/37.8267,-122.4233
"""

import requests
import datetime

def darksky_api_sf():
    print "Powered by Dark Sky"
    resp_darksky = requests.get(
        "https://api.darksky.net/forecast/61982b282ad0e8410101fb450a15edfc/37.8267,-122.4233"
        )
    print resp_darksky
    darksky_json = resp_darksky.json()
    curr_temp = darksky_json.get("currently").get("temperature")
    curr_summary = darksky_json.get("currently").get("summary")
    print curr_temp, curr_summary
    # print darksky_json.get("daily")
    for day in darksky_json.get("daily"):
        if datetime.datetime.fromtimestamp(
                int(day.get("time"))
            ).strftime("%m/%d") == "09/24":
            day_temp = day.get("temperature")
            day_summary = day.get("summary")
    print day_summary, day_temp

darksky_api_sf()