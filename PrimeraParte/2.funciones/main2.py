import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from calculadora2 import Ui_MainWindow  # tu archivo generado con pyuic5


# Clase para integrar matplotlib en PyQt
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Canvas de matplotlib dentro del verticalLayout
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.verticalLayout.addWidget(self.canvas)

        # Llenar el comboBox
        self.comboBox.addItems([
            "Seno", "Coseno", "Tangente", "Cotangente", "Secante", "Cosecante"
        ])

        # Conectar botón
        self.pushButton.clicked.connect(self.graficar)

    def graficar(self):
        try:
            minimo = float(self.lineEdit.text())
            maximo = float(self.lineEdit_2.text())

            if minimo >= maximo:
                QMessageBox.warning(self, "Error", "El mínimo debe ser menor que el máximo.")
                return

            x = np.linspace(np.deg2rad(minimo), np.deg2rad(maximo), 500)
            func = self.comboBox.currentText()

            if func == "Seno":
                y = np.sin(x)
            elif func == "Coseno":
                y = np.cos(x)
            elif func == "Tangente":
                y = np.tan(x)
            elif func == "Cotangente":
                y = 1 / np.tan(x)
            elif func == "Secante":
                y = 1 / np.cos(x)
            elif func == "Cosecante":
                y = 1 / np.sin(x)
            else:
                return

            # Graficar
            self.canvas.axes.clear()
            self.canvas.axes.plot(x, y, label=func)
            self.canvas.axes.legend()
            self.canvas.axes.grid(True)
            self.canvas.draw()

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingresa valores numéricos válidos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
