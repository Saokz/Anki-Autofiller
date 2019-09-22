import requests
from bs4 import BeautifulSoup

def translate(term=""):
	if term == "":
		return None
	url = "https://diksiyonaryo.ph/search/"+term
	result = ""

	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')

	word = soup.find('div', {'class': 'word'}, {'id': term})
	for sense in word.find_all('div', {'class': 'sense'}):
	    sense_content = sense.find('div', {'class': 'sense-content'})
	    definition = sense_content.find('span', {'class': 'definition'})
	    result+=definition.get_text()
	return result