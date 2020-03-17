import sys

from PyQt5.QtWidgets import *

from protocol_spec import Serial_Protocol


class GUIException(Exception):
    pass
        

class GUI(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.user_data = dict(
            data_len=88, #magic number
            date_font_color='',
            date_back_color='',
            clock_font_color='',
            clock_back_color=''
        )
        self.package = ''
        
    def initUI(self):
        setCOMPortButton = QPushButton("Настроить COM-порт")
        setDateFontColorButton = QPushButton("Задать цвет шрифта даты")
        setDateBackColorButton = QPushButton("Задать цвет фона даты")
        setClockFontButton = QPushButton("Задать цвет шрифта часов")
        setClockBackButton = QPushButton("Задать цвет фона часов")
        generatePackageButton = QPushButton("Создать пакет")
        showPackageInfoButton = QPushButton("Показать содержимое пакета")

        setCOMPortButton.setFixedSize(400, 35)
        setCOMPortButton.setFlat(True)
        setCOMPortButton.clicked.connect(self.showCOMDialog)

        generatePackageButton.clicked.connect(self.generatePackage)
        showPackageInfoButton.clicked.connect(self.showPackageInfo)

        setDateFontColorButton.clicked.connect(self.showColorDialog)
        setDateBackColorButton.clicked.connect(self.showColorDialog)
        setClockFontButton.clicked.connect(self.showColorDialog)
        setClockBackButton.clicked.connect(self.showColorDialog)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(setCOMPortButton, 1, 0)
        grid.addWidget(setFontColorButton, 2, 0)

        grid.addWidget(setBackgroundColorButton, 3, 0)
        
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

    def showPackageInfo(self):
        pass

    def showCOMDialog(self):
        text, ok = QInputDialog.getText(self, 'Настройка COM порта', 
            'Введите параметр:')

    def openColorDialog(self, attribute_name):
        color = QColorDialog.getColor()

        if color.isValid() and attribute_name in self.user_data:
            self.user_data[attribute_name] = color.name()
        else:
            raise GUIException('Color or given attribute name are not valid')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
