import requests
api_key = open("search_api_google_secret.txt").read()
search_engine_id = open('search_engine_id.txt').read()

search_queyr = '"founder" "@gmail.com" "London"'

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    "q": search_queyr,
    "key": api_key,
    "cx": search_engine_id
}

resonse= requests.get(url, params=params)
data= resonse.json()
print(data)
raju = 'raju'