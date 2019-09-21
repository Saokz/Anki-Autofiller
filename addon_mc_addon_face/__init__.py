from aqt import mw
from anki import notes
from aqt.utils import showInfo
from aqt.qt import *

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

    #Create a note with our model and populate it.
    n = notes.Note(mw.col, m)
    n.fields[0] = "bababooey search"        #This text is going to be temporary.
    n.fields[1] = "bababooey PinoyDict"     #This is where we use the webscrapers,
    n.fields[2] = "bababooey TagLessons"    #and the GUI to get user input for the
    n.fields[3] = "bababooey Diksiyonaryo"  #search term.

    mw.col.addNote(n)

# create a new menu item, "test"
action = QAction("Autofiller", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(autoFill)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
