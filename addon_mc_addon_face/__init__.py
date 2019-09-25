from aqt import mw
from anki import notes
#from aqt.utils import showInfo delete later
from aqt.utils import tooltip
from aqt.qt import * #change these imports to be more specific
from addonface import tagscrape #change addon folder name
import threading

def autoFill():
    models = mw.col.models

    #Search for the Autofiller model, and grab it
    m = models.byName("Autofiller")

    #if our Autofiller model doesn't exist, create one
    if m == None:
        #create a new model and add it to the list of models
        m = models.new(_("Autofiller"))
        models.addField(m, models.newField(_("Search Term") ))
        models.addField(m, models.newField(_("PinoyDict") ))
        models.addField(m, models.newField(_("TagalogLessons") ))
        models.addField(m, models.newField(_("Diksiyonaryo") ))

        #Create a card template. 'qfmt' is the front side of the card, 'afmt' the back
        t = models.newTemplate(_("Autofiller"))
        t['qfmt'] = "{{"+_("Search Term")+"}}"
        t['afmt'] = "{{"+_("Search Term")+"}}\n\n<hr id=answer>{{"+_("PinoyDict")+"}}<br>\n"+"{{"+_("TagalogLessons")+"}}<br>\n"+"{{"+_("Diksiyonaryo")+"}}"

        models.addTemplate(m, t) #necessary?
        models.add(m) #necessary?
    n = notes.Note(mw.col, m)

    #populate fields of note with the definitions
    results = tagscrape.translate("din")
    n.fields[0] = "din"
    n.fields[1] = results[0]
    n.fields[2] = results[1]
    n.fields[3] = results[2]
    
    #add note to the collection
    mw.col.addNote(n)
    tooltip("Added autofilled note")



# create a new menu item, "test"
action = QAction("Autofiller", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(autoFill)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
