# import the main window object (mw) from aqt
from aqt import mw
from anki import notes
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

def testFunction():

    m = mw.col.models

    autoModel = m.new(_("Autofiller"))
    srchField = m.newField(_("Search Term"))
    pinDict = m.newField(_("PinoyDict"))
    tagLess = m.newField(_("TagalogLessons"))
    diksy = m.newField(_("Diksiyonaryo"))
    m.addField(autoModel, srchField)
    m.addField(autoModel, pinDict)
    m.addField(autoModel, tagLess)
    m.addField(autoModel, diksy)

    autoT = m.newTemplate(_("Autofiller Template"))
    autoT['qfmt'] = "{{"+_("Search Term")+"}}"
    autoT['afmt'] = "{{"+_("Search Term")+"}}\n\n<hr id=answer>{{"+_("PinoyDict")+"}}<br>\n"+"{{"+_("TagalogLessons")+"}}<br>\n"+"{{"+_("Diksiyonaryo")+"}}"

    m.addTemplate(autoModel, autoT)
    m.add(autoModel)

    #need to add in a condition that checks to see if the autofiller template exists,
    #and adds it if necessary

    #figured out how to create a note and add information to it
    n = notes.Note(mw.col, autoModel)
    n.fields[0] = "bababooey search"
    n.fields[1] = "bababooey PinoyDict"
    n.fields[2] = "bababooey TagLessons"
    n.fields[3] = "bababooey Diksiyonaryo"

    mw.col.addNote(n)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
