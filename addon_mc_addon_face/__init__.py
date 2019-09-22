from aqt import mw
from anki import notes
from aqt.utils import showInfo
from aqt.utils import tooltip
from aqt.qt import * #change these imports to be more specific
from addonface import pinoydict
from addonface import diksiyonaryo
from addonface import taglessons
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

        models.addTemplate(m, t)
        models.add(m)

    pThread = threading.Thread(target=pinoydict.translate("din"))
    tThread = threading.Thread(target=taglessons.translate("din"))
    dThread = threading.Thread(target=diksiyonaryo.translate("din"))

    #Create a note with our model and populate it.
    n = notes.Note(mw.col, m)
    n.fields[0] = "din"  #This text is going to be temporary.
    n.fields[1] = pThread.start() #okay so this is a problem. thread.start() doesn't return anything
    n.fields[2] = tThread.start() #but we want the translate function to be threaded. And we want to
    n.fields[3] = dThread.start() #store the strings generated into these fields.

    mw.col.addNote(n)
    tooltip("Added autofilled note")

# create a new menu item, "test"
action = QAction("Autofiller", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(autoFill)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
