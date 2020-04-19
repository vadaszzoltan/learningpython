import requests
from datetime import datetime
from datetime import date
from datetime import timedelta

kezddatum = input("Kezdeit dátum:")

most = datetime.now()
#most = (most.strftime("%Y-%m-%d"))
print (most)

i = kezddatum
while i == most:
    url = "https://covid-193.p.rapidapi.com/history"
    querystring = {"day":i,"country":"romania"}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "e20da52ee3msh53287fe526ac8ddp11e8c2jsn79800f0ded7b"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    f=open("adat.txt", "a+")
    f.write(response.text)
    f.close()
    i = i + timedelta(days=1)
    print (i)