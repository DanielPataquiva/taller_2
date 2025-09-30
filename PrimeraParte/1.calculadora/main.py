import sys
import math
from PyQt5 import QtWidgets
from calculadora import Ui_MainWindow  # importa la clase generada por pyuic5

class Calculadora(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones a funciones
        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_mult.clicked.connect(self.multiplicar)
        self.btn_div.clicked.connect(self.dividir)
        self.btn_residuo.clicked.connect(self.residuo)

        self.btn_seno.clicked.connect(self.seno)
        self.btn_coseno.clicked.connect(self.coseno)
        self.btn_tan.clicked.connect(self.tangente)
        self.btn_cot.clicked.connect(self.cotangente)
        self.btn_sec.clicked.connect(self.secante)
        self.btn_csc.clicked.connect(self.cosecante)

    # --- Funciones auxiliares ---
    def get_values(self):
        try:
            v1 = float(self.lineEdit_valor1.text())
            v2 = float(self.lineEdit_valor2.text()) if self.lineEdit_valor2.text() else 0
            return v1, v2
        except:
            self.label_resultado.setText("Error: ingrese números")
            return None, None

    # --- Operaciones aritméticas ---
    def sumar(self):
        v1, v2 = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(v1 + v2))

    def restar(self):
        v1, v2 = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(v1 - v2))

    def multiplicar(self):
        v1, v2 = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(v1 * v2))

    def dividir(self):
        v1, v2 = self.get_values()
        if v1 is not None:
            if v2 == 0:
                self.label_resultado.setText("Error: división por 0")
            else:
                self.label_resultado.setText(str(v1 / v2))

    def residuo(self):
        v1, v2 = self.get_values()
        if v1 is not None:
            if v2 == 0:
                self.label_resultado.setText("Error: división por 0")
            else:
                self.label_resultado.setText(str(v1 % v2))

    # --- Funciones trigonométricas ---
    def seno(self):
        v1, _ = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(math.sin(math.radians(v1))))

    def coseno(self):
        v1, _ = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(math.cos(math.radians(v1))))

    def tangente(self):
        v1, _ = self.get_values()
        if v1 is not None:
            self.label_resultado.setText(str(math.tan(math.radians(v1))))

    def cotangente(self):
        v1, _ = self.get_values()
        if v1 is not None:
            if math.tan(math.radians(v1)) == 0:
                self.label_resultado.setText("Indefinido")
            else:
                self.label_resultado.setText(str(1 / math.tan(math.radians(v1))))

    def secante(self):
        v1, _ = self.get_values()
        if v1 is not None:
            if math.cos(math.radians(v1)) == 0:
                self.label_resultado.setText("Indefinido")
            else:
                self.label_resultado.setText(str(1 / math.cos(math.radians(v1))))

    def cosecante(self):
        v1, _ = self.get_values()
        if v1 is not None:
            if math.sin(math.radians(v1)) == 0:
                self.label_resultado.setText("Indefinido")
            else:
                self.label_resultado.setText(str(1 / math.sin(math.radians(v1))))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())
