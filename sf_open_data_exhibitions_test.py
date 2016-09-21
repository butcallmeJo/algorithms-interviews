# 2) By using the SF Open data API of Museum Exhibitions (https://data.sfgov.org/resource/4qkm-qtkz.json), please provide:
# - number of exhibitions starting 2015
# - list of exhibition titles starting in January 2015
# - list all differents Gallery area
# - list of title exhibitions at the date: 2015-03-23 (start before and not finish at this date)


## CODE HERE
import requests
import datetime

resp = requests.get("https://data.sfgov.org/resource/4qkm-qtkz.json")
resp_json = resp.json()
num_exhibitions_2015 = 0
list_exhibitions_titles_jan_2015 = []
list_diff_gallery_areas = []
list_exhibition_titles_open_at_date = []

for ex in resp_json:
    if ex.get("start_date_year") == '2015':
        num_exhibitions_2015 += 1
        if ex.get("start_date_month") == '1':
            list_exhibitions_titles_jan_2015.append(ex.get("title"))
    if ex.get("gallery_area") not in list_diff_gallery_areas and \
    ex.get("gallery_area"):
        list_diff_gallery_areas.append(ex.get("gallery_area"))
    if ex.get("start_date") and ex.get("end_date"):
        start_date = datetime.datetime.strptime(
            ex.get("start_date")[:-13], "%Y-%m-%d"
        )
        end_date = datetime.datetime.strptime(
            ex.get("end_date")[:-13], "%Y-%m-%d"
        )
        compare_date = datetime.datetime.strptime(
            "2015-03-23", "%Y-%m-%d"
        )
        if start_date <= compare_date < end_date:
            list_exhibition_titles_open_at_date.append(ex.get("title"))

print num_exhibitions_2015
print ", ".join(list_exhibitions_titles_jan_2015)
print ", ".join(list_diff_gallery_areas)
print ", ".join(list_exhibition_titles_open_at_date)