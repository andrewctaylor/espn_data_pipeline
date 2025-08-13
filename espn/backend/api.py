import requests

# API Call -> general blanket API Call
def api_call(sport,league,type):
    url = f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/{type}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{sport}/{league} call successful")
        return data
    else:
        print(f"Request failed for {sport}/{league} with status: {response.status_code}") 
        

# API Call -> json object of espn news
def fetch_articles():
    url = "http://now.core.api.espn.com/v1/sports/news"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


