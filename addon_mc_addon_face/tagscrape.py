import requests
from bs4 import BeautifulSoup

def translate(term=""):
	if term == "":
		return None
	results = ["","",""]
	url_1 = "https://tagalog.pinoydictionary.com/search?q="+term
	url_2 = "https://tagaloglessons.com/ajax/reference_guide_search_results2.php?keyword=" + term + "&num_results=10&no_search_login=false"
	url_3 = "https://diksiyonaryo.ph/search/"+term

	#scrape pinoydict
	data = requests.get(url_1)
	soup = BeautifulSoup(data.text, 'html.parser')
	definition = soup.find('div', {'class': 'definition'}).get_text()
	results[0] = definition

	#scrape taglessons
	data = requests.get(url_2)
	soup = BeautifulSoup(data.text, 'html.parser')
	div = soup.find_all('div')[3].get_text()
	extra = soup.find_all('div')[3].find_all('a')[2].get_text()
	results[1] = div.split(extra)[0]

	#scrape diksiyonaryo
	data = requests.get(url_3)
	soup = BeautifulSoup(data.text, 'html.parser')
	word = soup.find('div', {'class': 'word'}, {'id': term})
	for sense in word.find_all('div', {'class': 'sense'}):
	    sense_content = sense.find('div', {'class': 'sense-content'})
	    definition = sense_content.find('span', {'class': 'definition'})
	    results[2]+=definition.get_text()
	
	return results

