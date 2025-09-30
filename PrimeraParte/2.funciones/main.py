import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from calculadora import Ui_MainWindow  # tu UI generado


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

        # Insertar canvas de matplotlib en el widgetGrafica
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QVBoxLayout(self.widgetGrafica)
        layout.addWidget(self.canvas)

        # Llenar ComboBox con funciones trigonométricas
        self.comboFunciones.addItems([
            "Seno", "Coseno", "Tangente", "Cotangente", "Secante", "Cosecante"
        ])

        # Valores iniciales para probar
        self.txtMin.setText("0")
        self.txtMax.setText("0")

        # Conectar el botón
        self.btnGraficar.clicked.connect(self.graficar)

    def graficar(self):
        try:
            minimo = float(self.txtMin.text())
            maximo = float(self.txtMax.text())

            if minimo >= maximo:
                print("El mínimo debe ser menor que el máximo.")
                return

            x = np.linspace(minimo, maximo, 500)
            func = self.comboFunciones.currentText()

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

            # Limpiar e imprimir nueva gráfica
            self.canvas.axes.clear()
            self.canvas.axes.plot(x, y, label=func)
            self.canvas.axes.legend()
            self.canvas.axes.grid(True)
            self.canvas.draw()

        except Exception as e:
            print("Error en graficar:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())