import requests
from bs4 import BeautifulSoup

def translate(term=""):
	if term == "":
		return None
	url = "https://tagalog.pinoydictionary.com/search?q="+term

	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')
	definition = soup.find('div', {'class': 'definition'}).get_text()

	return definition