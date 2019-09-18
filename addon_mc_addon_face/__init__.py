# import the main window object (mw) from aqt
from aqt import mw
from anki import notes
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window

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

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
