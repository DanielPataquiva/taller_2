import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from robots import Ui_MainWindow  # IMPORTA el archivo generado desde robots.ui


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

        # Canvas de Matplotlib dentro del widget
        self.canvas = MplCanvas(self.widgetGrafica, width=5, height=4, dpi=100)
        layout = QVBoxLayout(self.widgetGrafica)
        layout.addWidget(self.canvas)

        # Llenar el combo con los tipos de robot
        self.comboRobots.addItems(["Cartesiano", "Cilíndrico", "Esférico"])

        # Conectar evento
        self.btnMostrar.clicked.connect(self.mostrar_robot)

    def mostrar_robot(self):
        robot = self.comboRobots.currentText()

        # Limpiar gráfica
        self.canvas.axes.clear()

        if robot == "Cartesiano":
            self.labelInfo.setText("Robot cartesiano: 3 articulaciones prismáticas (lineales).")
            self.canvas.axes.plot([0, 1], [0, 0], "r-", linewidth=3)
            self.canvas.axes.plot([1, 1], [0, 1], "g-", linewidth=3)
            self.canvas.axes.plot([1, 2], [1, 1], "b-", linewidth=3)

        elif robot == "Cilíndrico":
            self.labelInfo.setText("Robot cilíndrico: 1 rotacional + 2 prismáticas.")
            import matplotlib.patches as patches
            circle = patches.Circle((0, 0), 0.5, fill=False, color="blue")
            self.canvas.axes.add_patch(circle)
            self.canvas.axes.plot([0, 0], [0, 2], "g-", linewidth=3)
            self.canvas.axes.plot([0, 1], [2, 2], "r-", linewidth=3)

        elif robot == "Esférico":
            self.labelInfo.setText("Robot esférico: 2 rotacionales + 1 prismática.")
            import matplotlib.patches as patches
            arc = patches.Arc((0, 0), 2, 2, theta1=0, theta2=90, color="red")
            self.canvas.axes.add_patch(arc)
            self.canvas.axes.plot([0, 1], [0, 1], "g-", linewidth=3)
            self.canvas.axes.plot([1, 1], [1, 2], "b-", linewidth=3)

        # Redibujar
        self.canvas.axes.set_aspect("equal", adjustable="box")
        self.canvas.axes.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
