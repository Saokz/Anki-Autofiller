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

    testModel = m.new(_("Test"))
    testField1 = m.newField(_("TestField1"))
    testField2 = m.newField(_("TestField2"))
    testField3 = m.newField(_("TestField3"))
    testField4 = m.newField(_("TestField4"))
    m.addField(testModel, testField1)
    m.addField(testModel, testField2)
    m.addField(testModel, testField3)
    m.addField(testModel, testField4)

    t = m.newTemplate(_("Test Template"))
    t['qfmt'] = "{{"+_("TestField1")+"}}"
    t['afmt'] = "{{"+_("TestField2")+"}}"
    t['bqfmt'] = "{{"+_("TestField3")+"}}"
    t['bafmt'] = "{{"+_("TestField4")+"}}"

    m.addTemplate(testModel, t)
    m.add(testModel)

    """
    Right. You figured out how to do the thing. Add the multiple fields.

    But you gotta learn more about how to make templates. They're made using HTML.
    So you gotta learn some HTML.

	Then you'll be done with the "create a custom model thing". And then be pretty close to
	"create a custom note thing"
    """




   



# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
