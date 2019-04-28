
from PyQt5 import QtWidgets
from pyquery import PyQuery as pq
import os.path

INHERITED_ATTRS = ('_returns',)

class Meta(type):
    def __new__(meta, name, bases, attrs):
        parent = type.__new__(meta, name, bases, {})
        for key, value in list(attrs.items()):
            if not key.startswith('__') and callable(value):
                value = propagate(getattr(parent, key, None), value)
                print("key: %s, value: %s" % (key, value))
        #print("cls %s, name %s, base %s, attrs %s " % (cls, name, bases, attrs))
        return type.__new__(meta, name, bases, attrs)

def propagate(method1, method2):
    if method1:
        for attr in INHERITED_ATTRS:
            if hasattr(method1, attr) and not hasattr(method2, attr):
                setattr(method2, attr, getattr(method1, attr))
    return method2


class Base(Meta('DummyModel', (object,),{})):
    _name = False


class Cascada(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.doc = None
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.base = Base()
    
    def run(self):
        self.initGUI()

    def initGUI(self):
        #self.load_template('layout.html')
        self.document = self.get_document()
        self.title = self.document("title").text()
        # TODO: Use expreg for match extend file
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def set_document(self, document):
        self.doc = document

    def get_document(self):
        return self.doc

    def load_template(self, template):
        if not isinstance(template, str):
            raise Exception("Could't load template %s, this requires a string args, instead of %s"
                    % (template, type(template))) # TODO: create custom error
        with open(os.path.join("templates", template), 'r') as f:
            contents = f.read()
            document = pq(contents)
            self.set_document(document)
    
