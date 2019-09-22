import requests
from bs4 import BeautifulSoup

def translate(term=""):
	if term == "":
		return None
	url = "https://tagaloglessons.com/ajax/reference_guide_search_results2.php?keyword=" + term + "&num_results=10&no_search_login=false"

	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')
	div = soup.find_all('div')[3].get_text()
	extra = soup.find_all('div')[3].find_all('a')[2].get_text()

	return div.split(extra)[0]