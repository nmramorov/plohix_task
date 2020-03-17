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
            date_font_color=0,
            date_back_color=0,
            clock_font_color=0,
            clock_back_color=0
        )
        self.package = ''
        
        self.initUI()

        
    def initUI(self):
        self.label = QLabel()

        self.generateButtons()
        self.setButtonsActivities()

        gui_grid = self.setGrid()
        self.setLayout(gui_grid)
        
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
        self.showPackageInfoButton.setDisabled(0)

    def showPackageInfo(self):
        self.label.setText(str(self.package))

    def showCOMDialog(self):
        text, ok = QInputDialog.getText(self, 'Настройка COM порта', 'Введите параметр:')

    def showColorDialog(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()
        if self.setDateFontColorButton.isActiveWindow():
            self.user_data['date_font_color'] = color.name()
        elif self.setDateBackColorButton.isActiveWindow():
            self.user_data['date_back_color'] = color.name()
        elif self.setClockFontButton.isActiveWindow():
            self.user_data['clock_font_color'] = color.name()
        elif self.setClockBackButton.isActiveWindow():
            self.user_data['clock_back_color'] = color.name()

    def encodeColors(self, color):
        pass

    def generateButtons(self):
        self.setCOMPortButton = QPushButton("Настроить COM-порт")
        self.setDateFontColorButton = QPushButton("Задать цвет шрифта даты")
        self.setDateBackColorButton = QPushButton("Задать цвет фона даты")
        self.setClockFontButton = QPushButton("Задать цвет шрифта часов")
        self.setClockBackButton = QPushButton("Задать цвет фона часов")
        self.generatePackageButton = QPushButton("Создать пакет")
        self.showPackageInfoButton = QPushButton("Показать содержимое пакета")
        self.showPackageInfoButton.setDisabled(1)

    def setButtonsActivities(self):
        self.setCOMPortButton.clicked.connect(self.showCOMDialog)

        self.generatePackageButton.clicked.connect(self.generatePackage)
        self.showPackageInfoButton.clicked.connect(self.showPackageInfo)

        self.setDateFontColorButton.clicked.connect(self.showColorDialog)
        self.setDateBackColorButton.clicked.connect(self.showColorDialog)
        self.setClockFontButton.clicked.connect(self.showColorDialog)
        self.setClockBackButton.clicked.connect(self.showColorDialog)

    def setGrid(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label)

        grid.addWidget(self.setCOMPortButton, 1, 0)
        grid.addWidget(self.setDateFontColorButton, 2, 0)
        grid.addWidget(self.setDateBackColorButton, 3, 0)
        grid.addWidget(self.setClockFontButton, 4, 0)
        grid.addWidget(self.setClockBackButton, 1, 1)
        grid.addWidget(self.generatePackageButton, 2, 1)
        grid.addWidget(self.showPackageInfoButton, 3, 1)
        return grid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
