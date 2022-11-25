import requests
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
response = requests.get("http://ip-api.com/json/?fields=66846719&lang=en").json()


print("Ip Address: "+ip+"\nCountry: "+response["country"]+"\nCurrency: "+response["currency"]+"\nCountry Code: "+str(response["countryCode"])+"\nRegion Name: "+response["regionName"]+"\nCity: "+response["city"]+"\nLatitude: "+str(response["lat"])+"\nLongitude"+str(response["lon"])+"\nAsn: "+response["as"]+"\nIsp: "+response["isp"])

