from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from bs4 import BeautifulSoup
import requests

#So far addon adds an item in the "tools" menu that searches diksiyonaryo
#for the word "din" and returns the results in a new window

def testFunction():

	url = "https://diksiyonaryo.ph/search/"+"din"
	response = ""

	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')

	word = soup.find('div', {'class': 'word'}, {'id': 'din'})
	for sense in word.find_all('div', {'class': 'sense'}):
		sense_content = sense.find('div', {'class': 'sense-content'})
		definition = sense_content.find('span', {'class': 'definition'})
		response += definition.get_text()


	showInfo("Word definition: %s" % response)

action = QAction("test", mw)
action.triggered.connect(testFunction)
mw.form.menuTools.addAction(action)