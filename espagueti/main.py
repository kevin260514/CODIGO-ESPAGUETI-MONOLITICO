import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QLineEdit,
                              QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

cobijas = []

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tienda de Cobijas - ESPAGUETI")
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        titulo = QLabel("INVENTARIO DE COBIJAS (M_E)")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #c0392b;")
        layout.addWidget(titulo)

        self.campo_nombre = QLineEdit()
        self.campo_nombre.setPlaceholderText("TIPO DE COBIJA")
        layout.addWidget(self.campo_nombre)

        self.campo_precio = QLineEdit()
        self.campo_precio.setPlaceholderText("Precio")
        layout.addWidget(self.campo_precio)

        self.campo_cantidad = QLineEdit()
        self.campo_cantidad.setPlaceholderText("Cantidad")
        layout.addWidget(self.campo_cantidad)

        btn_layout = QHBoxLayout()

        btn_agregar = QPushButton("Agregar")
        btn_agregar.setStyleSheet("background-color: #27ae60; color: white; padding: 8px;")
        btn_agregar.clicked.connect(self.agregar)
        btn_layout.addWidget(btn_agregar)

        btn_eliminar = QPushButton("Eliminar")
        btn_eliminar.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px;")
        btn_eliminar.clicked.connect(self.eliminar)
        btn_layout.addWidget(btn_eliminar)

        btn_editar = QPushButton("Editar Producto")
        btn_editar.setStyleSheet("background-color: #f39c12; color: white; padding: 8px;")
        btn_editar.clicked.connect(self.editar)
        btn_layout.addWidget(btn_editar)

        layout.addLayout(btn_layout)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Precio", "Cantidad"])
        self.tabla.setColumnWidth(0, 200)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        layout.addWidget(self.tabla)

        widget.setLayout(layout)

    def agregar(self):
        nombre = self.campo_nombre.text()
        precio = self.campo_precio.text()
        cantidad = self.campo_cantidad.text()

        if not nombre or not precio or not cantidad:
            QMessageBox.warning(self, "Error", "Rellena todos los campos")
            return

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except:
            QMessageBox.warning(self, "Error", "Precio o cantidad inválidos")
            return

        cobijas.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        QMessageBox.information(self, "Éxito", f"Cobija '{nombre}' agregada")
        self.campo_nombre.clear()
        self.campo_precio.clear()
        self.campo_cantidad.clear()
        self.actualizar_tabla()

    def eliminar(self):
        nombre = self.campo_nombre.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Escribe el nombre a eliminar")
            return

        encontrado = False
        for i, c in enumerate(cobijas):
            if c["nombre"].lower() == nombre.lower():
                cobijas.pop(i)
                encontrado = True
                break

        if encontrado:
            QMessageBox.information(self, "Éxito", f"Cobija '{nombre}' eliminada")
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Error", f"No se encontró '{nombre}'")

    def editar(self):
        nombre = self.campo_nombre.text()
        nuevo_precio = self.campo_precio.text()
        nueva_cantidad = self.campo_cantidad.text()

        if not nombre:
            QMessageBox.warning(self, "Error", "Escribe el nombre de la cobija a editar")
            return

        if not nuevo_precio or not nueva_cantidad:
            QMessageBox.warning(self, "Error", "Escribe el nuevo precio y cantidad")
            return

        try:
            nuevo_precio = float(nuevo_precio)
            nueva_cantidad = int(nueva_cantidad)
        except:
            QMessageBox.warning(self, "Error", "Precio o cantidad inválidos")
            return

        encontrado = False
        for c in cobijas:
            if c["nombre"].lower() == nombre.lower():
                c["precio"] = nuevo_precio
                c["cantidad"] = nueva_cantidad
                encontrado = True
                break

        if encontrado:
            QMessageBox.information(self, "Éxito", f"Cobija '{nombre}' actualizada correctamente")
            self.campo_nombre.clear()
            self.campo_precio.clear()
            self.campo_cantidad.clear()
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Error", f"No se encontró '{nombre}'")

    def actualizar_tabla(self):
        self.tabla.setRowCount(len(cobijas))
        for i, c in enumerate(cobijas):
            self.tabla.setItem(i, 0, QTableWidgetItem(c["nombre"]))
            self.tabla.setItem(i, 1, QTableWidgetItem(f"${c['precio']:.2f}"))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(c["cantidad"])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())