
from PyQt5 import QtWidgets
from pyquery import PyQuery as pq
import os.path
from cascabel import api


class Base(api.Meta('DummyModel', (object,),{})):
    _name = False

    def load_template(self):
        pass


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
    
