import sys

from PyQt5.QtWidgets import *

from src.protocol.protocol_spec import Serial_Protocol


PACKAGE_DATA_LENGTH = 88

class GUIException(Exception):
    pass


class GUI(QWidget):
    
    def __init__(self):
        super().__init__()
        self.user_data = dict(
            data_len=PACKAGE_DATA_LENGTH,  # magic number
            date_font_color=4,
            date_back_color=2,
            clock_font_color=3,
            clock_back_color=5
        )
        self.package = ''
        
        self.initUI()

        
    def initUI(self):
        setCOMPortButton = QPushButton("Настроить COM-порт")
        setDateFontColorButton = QPushButton("Задать цвет шрифта даты")
        setDateBackColorButton = QPushButton("Задать цвет фона даты")
        setClockFontButton = QPushButton("Задать цвет шрифта часов")
        setClockBackButton = QPushButton("Задать цвет фона часов")
        generatePackageButton = QPushButton("Создать пакет")
        showPackageInfoButton = QPushButton("Показать содержимое пакета")

        self.label = QLabel()

        setCOMPortButton.clicked.connect(self.showCOMDialog)

        generatePackageButton.clicked.connect(self.generatePackage)
        showPackageInfoButton.clicked.connect(self.showPackageInfo)

        setDateFontColorButton.clicked.connect(self.showColorDialog)
        setDateBackColorButton.clicked.connect(self.showColorDialog)
        setClockFontButton.clicked.connect(self.showColorDialog)
        setClockBackButton.clicked.connect(self.showColorDialog)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label)

        grid.addWidget(setCOMPortButton, 1, 0)
        grid.addWidget(setDateFontColorButton, 2, 0)
        grid.addWidget(setDateBackColorButton, 3, 0)
        grid.addWidget(setClockFontButton, 4, 0)
        grid.addWidget(setClockBackButton, 1, 1)
        grid.addWidget(generatePackageButton, 2, 1)
        grid.addWidget(showPackageInfoButton, 3, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Mramorov-Volkov-Martinova')    
        self.show()

    def generatePackage(self):
        p = Serial_Protocol(self.user_data['data_len'],
                            self.user_data['date_font_color'],
                            self.user_data['date_back_color'],
                            self.user_data['clock_font_color'],
                            self.user_data['clock_back_color'])
        self.package = p.init_package()
        self.label.setText('Пакет создан')

    def showPackageInfo(self):
        self.label.setText(str(self.package))

    def showCOMDialog(self):
        text, ok = QInputDialog.getText(self, 'Настройка COM порта', 'Введите параметр:')

    def showColorDialog(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
