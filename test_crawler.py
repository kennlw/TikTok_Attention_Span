import requests

url = "https://tiktok-best-experience.p.rapidapi.com/trending/US"

querystring = {"custom_cursor":"12"}

headers = {
	"X-RapidAPI-Key": "0ae27abe0cmsha7512d2059572d1p136488jsn01d8cf8cc1ea",
	"X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())