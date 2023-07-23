import requests

url = "https://tiktok-best-experience.p.rapidapi.com/trending/US"

querystring = {"custom_cursor":"12"}

headers = {
	"X-RapidAPI-Key": "_",
	"X-RapidAPI-Host": "tiktok-best-experience.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
