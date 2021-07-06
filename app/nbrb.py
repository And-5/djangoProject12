import requests
import json


def rate():
    response = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-06-20&enddate=2021-06-25')
    price = json.loads(response.text)
    rate_sum = 0
    for i in price:
        rate = i['Cur_OfficialRate']
        rate_sum += rate
        average_rate = round(rate_sum / 7, 3)
    return average_rate
a = rate()
print(a)