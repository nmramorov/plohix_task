# plohix_task

Создание пакета реализовано с помощью двух файлов: [protocol_spec.py](https://github.com/nmramorov/plohix_task/blob/develop/src/protocol/protocol_spec.py) и [package_protocol_spec.py](https://github.com/nmramorov/plohix_task/blob/develop/src/protocol/package_spec.py)

Графический интерфейс пользователя реализован в файле [interface.py](https://github.com/nmramorov/plohix_task/blob/develop/src/gui/interface.py)

Для запуска программы необходимо выполнить следующие действия:

1. Проверить текущую версию __Python__ (Если интерпретатор не установлен, его можно скачатб по [ссылке](https://www.python.org/downloads/)
   Для этого необходимо ввести в терминале (или в консоли CMD) команду:
   ```
   python --version
   ```
2. Установить зависимости командой:
   ```
   pip install bitstring PyQt5
   ```
3. Запустить файл __interface.py__, находящийся в папке __src/gui/inteface.py__, командой:
   ```
   python -m interface.py
   ```
   Либо просто нажав на него два раза кнопкой мыши