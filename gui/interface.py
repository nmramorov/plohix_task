import sys

from PyQt5.QtWidgets import *


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        setCOMPortButton = QPushButton("Настроить COM-порт")
        setFontColorButton = QPushButton("Задать цвет шрифта")
        setBackgroundColorButton = QPushButton("Задать цвет фона")

        setCOMPortButton.setFixedSize(400, 35)
        setCOMPortButton.setFlat(True)
        setCOMPortButton.clicked.connect(self.showCOMDialog)

        setFontColorButton.clicked.connect(self.showColorDialog)
        setBackgroundColorButton.clicked.connect(self.showColorDialog)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(setCOMPortButton, 1, 0)
        grid.addWidget(setFontColorButton, 2, 0)

        grid.addWidget(setBackgroundColorButton, 3, 0)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Mramorov-Volkov-Martinova')    
        self.show()

    def showCOMDialog(self):
        text, ok = QInputDialog.getText(self, 'Настройка COM порта', 
            'Введите параметр:')

    def showColorDialog(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
