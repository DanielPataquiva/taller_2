import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from rc import Ui_MainWindow  # generado con pyuic5


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # insertar matplotlib en widgetGrafica
        self.canvas = MplCanvas(self.widgetGrafica, width=5, height=4, dpi=100)
        layout = QVBoxLayout(self.widgetGrafica)
        layout.addWidget(self.canvas)

        # conectar sliders
        self.sliderR.valueChanged.connect(self.actualizar_labels)
        self.sliderC.valueChanged.connect(self.actualizar_labels)
        self.sliderV.valueChanged.connect(self.actualizar_labels)

        # conectar botón
        self.btnSimular.clicked.connect(self.iniciar_simulacion)

        # timer para graficar en tiempo real
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.t = 0

        self.actualizar_labels()

    def actualizar_labels(self):
        self.valueR.setText(str(self.sliderR.value()))
        self.valueC.setText(str(self.sliderC.value()))
        self.valueV.setText(str(self.sliderV.value()))

    def iniciar_simulacion(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnSimular.setText("Simular")
        else:
            self.t = 0
            self.canvas.axes.clear()
            self.timer.start(50)  # 50ms
            self.btnSimular.setText("Detener")

    def update_plot(self):
        R = self.sliderR.value()
        C = self.sliderC.value() * 1e-6  # microfaradios
        V = self.sliderV.value()

        tau = R * C
        t = np.linspace(0, 5 * tau, 200)

        # graficar carga y descarga
        carga = V * (1 - np.exp(-t / tau))
        descarga = V * np.exp(-t / tau)

        self.canvas.axes.clear()
        self.canvas.axes.plot(t, carga, label="Carga")
        self.canvas.axes.plot(t, descarga, label="Descarga")
        self.canvas.axes.set_xlabel("Tiempo (s)")
        self.canvas.axes.set_ylabel("Voltaje (V)")
        self.canvas.axes.legend()
        self.canvas.axes.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
