import requests
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
response = requests.get("http://ip-api.com/json/"+ip).json()

print("query: "+ip+"\ncountry: "+response["country"]+"\ncountryCode: "+str(response["countryCode"])+"\nregionName: "+response["regionName"]+"\ncity: "+response["city"]+"\nlatitude: "+str(response["lat"])+"\nlongitude"+str(response["lon"])+"\nasn: "+response["as"]+"\nisp: "+response["isp"])