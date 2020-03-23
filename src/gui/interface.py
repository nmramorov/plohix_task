import sys

from PyQt5.QtWidgets import *

from src.protocol.protocol_spec import SerialProtocol


PACKAGE_DATA_LENGTH = 88
RGB_COLOR_DEFINITIONS = dict(
    black      =    ('#000000', 0),
    navy       =    ('#000080', 1),
    dark_green =    ('#008000', 2),
    dark_cyan  =    ('#008080', 3),
    maroon     =    ('#800000', 4),
    purple     =    ('#800080', 5),
    olive      =    ('#808000', 6),
    light_grey =    ('#c0c0c0', 7),
    dark_grey  =    ('#808080', 8),
    blue       =    ('#0000ff', 9),
    green      =    ('#00ff00',10),
    cyan       =    ('#00ffff',11),
    red        =    ('#ff0000',12),
    magenta    =    ('#ff00ff',13),
    yellow     =    ('#ffff00',14),
    white      =    ('#ffffff',15),
)


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
        self.label = QLabel()
        self.pressed_button = ''
        self.initUI()

    def initUI(self):
        self.generateButtons()
        self.setButtonsActivities()

        gui_grid = self.setGrid()
        self.setLayout(gui_grid)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Mramorov-Volkov-Martinova')
        self.show()

    def generatePackage(self):
        p = SerialProtocol(self.user_data['data_len'],
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

    def showDateFontColorDialog(self):
        self.pressed_button = 'date_font_color_button'
        self.openColorDialog()

    def showDateBackColorDialog(self):
        self.pressed_button = 'date_back_color_button'
        self.openColorDialog()

    def showClockFontColorDialog(self):
        self.pressed_button = 'clock_font_color_button'
        self.openColorDialog()

    def showClockBackolorDialog(self):
        self.pressed_button = 'clock_back_color_button'
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()
        self.encodeColor(color.name())

    def encodeColor(self, color_name):
        for color_code, encoded_color in RGB_COLOR_DEFINITIONS.values():
            if color_name == color_code:
                if self.pressed_button == 'date_font_color_button':
                    self.user_data['date_font_color'] = encoded_color
                elif self.pressed_button == 'date_back_color_button':
                    self.user_data['date_back_color'] = encoded_color
                elif self.pressed_button == 'clock_font_color_button':
                    self.user_data['clock_font_color'] = encoded_color
                elif self.pressed_button == 'clock_font_color_button':
                    self.user_data['clock_back_color'] = encoded_color

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
        self.setDateFontColorButton.clicked.connect(self.showDateFontColorDialog)
        self.setDateBackColorButton.clicked.connect(self.showDateBackColorDialog)
        self.setClockFontButton.clicked.connect(self.showClockFontColorDialog)
        self.setClockBackButton.clicked.connect(self.showClockBackolorDialog)

    def setGrid(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.label)
        grid.addWidget(self.setCOMPortButton,       1, 0)
        grid.addWidget(self.setDateFontColorButton, 2, 0)
        grid.addWidget(self.setDateBackColorButton, 3, 0)
        grid.addWidget(self.setClockFontButton,     4, 0)
        grid.addWidget(self.setClockBackButton,     1, 1)
        grid.addWidget(self.generatePackageButton,  2, 1)
        grid.addWidget(self.showPackageInfoButton,  3, 1)
        return grid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
