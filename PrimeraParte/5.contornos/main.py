import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from contornos import Ui_MainWindow  # generado con pyuic5


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnCargar.clicked.connect(self.cargar_imagen)

    def cargar_imagen(self):
        # abrir selector de archivos
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )
        if ruta:
            # cargar imagen en cv2
            img = cv2.imread(ruta)
            if img is None:
                return

            # mostrar imagen original
            self.mostrar_imagen(img, self.labelOriginal)

            # procesar contornos
            gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, binaria = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY)
            contornos, _ = cv2.findContours(
                binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            img_contornos = img.copy()
            cv2.drawContours(img_contornos, contornos, -1, (0, 255, 0), 2)

            # mostrar imagen con contornos
            self.mostrar_imagen(img_contornos, self.labelContornos)

    def mostrar_imagen(self, img, label):
        # convertir BGR -> RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        # ajustar al tamaño del QLabel
        label.setPixmap(pixmap.scaled(label.width(), label.height()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
