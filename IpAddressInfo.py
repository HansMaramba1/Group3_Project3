@@ -0,0 +1,7 @@
import requests
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
response = requests.get("http://ip-api.com/json/?fields=66846719&lang=en").json()

print("query: "+ip+"\ncountry: "+response["country"]+"\ncountryCode: "+str(response["countryCode"])+"\nregionName: "+response["regionName"]+"\ncity: "+response["city"]+"\nCurrency: "+str(response["currency"])+"\nlatitude: "+str(response["lat"])+"\nlongitude"+str(response["lon"])+"\nasn: "+response["as"]+"\nisp: "+response["isp"])
