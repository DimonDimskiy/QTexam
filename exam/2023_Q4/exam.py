import psutil

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUI(self):
        """

        """
        self.systemPlaintextEdit = QtWidgets.QPlainTextEdit()
        self.cpuNameLabel = QtWidgets.QLabel("Название процессора:")
        self.cpuLogicCoresLabel = QtWidgets.QLabel(f"Логических ядер:{psutil.cpu_count(logical=True)}")
        self.cpuPhysicCoresLabel = QtWidgets.QLabel(f"Физических ядер:{psutil.cpu_count(logical=False)}")
        self.cpuLoadLabel = QtWidgets.QLabel(f"Загрузка процессора:{psutil.cpu_percent()} %")
        self.ramInfoLabel = QtWidgets.QLabel("Оперативной памяти:")
        self.ramLoadLabel = QtWidgets.QLabel("Использовано памяти:")
        self.diskCountLabel = QtWidgets.QLabel("Количество дисков:")


class SystemViewerTread(QtCore.QThread):
    systemInfoReceived = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
        self.delay = None
        while True:
            self.data["Название процессора:"] = psutil
            self.data["Логических ядер:"] = psutil.cpu_count(logical=True)
            self.data["Физических ядер:"] = psutil.cpu_count(logical=False)
            self.data["Загрузка процессора, %:"] = psutil.cpu_percent()
            self.data["Оперативной памяти:"] =
            ram_value =
            self.systemSignal  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time}

print(psutil.cpu_stats())
