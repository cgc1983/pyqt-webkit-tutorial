import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        view = QWebView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(view)

        html = """
            <html><body>
            Hello World!
            </body></html>
            """
        view.setHtml(html)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
