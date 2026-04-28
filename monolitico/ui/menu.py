import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QLineEdit,
                              QTableWidget, QTableWidgetItem, QMessageBox)
from services.cobija_service import CobijaService

class VentanaPrincipal(QMainWindow):
    #delega toda la logica al servicio

    def __init__(self):
        super().__init__()
        self.service = CobijaService()
        self.setWindowTitle("Tienda de Cobijas -Monolitico")
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        titulo = QLabel(" Inventario de Cobijas (Arquitectura por Capas-monolitico)")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2980b9;")
        layout.addWidget(titulo)

        self.campo_nombre = QLineEdit()
        self.campo_nombre.setPlaceholderText("Nombre de la cobija")
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
        ok, mensaje = self.service.agregar_cobija(
            self.campo_nombre.text(),
            self.campo_precio.text(),
            self.campo_cantidad.text()
        )
        if ok:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar(self):
        ok, mensaje = self.service.eliminar_cobija(self.campo_nombre.text())
        if ok:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def editar(self):
        ok, mensaje = self.service.editar_cobija(
            self.campo_nombre.text(),
            self.campo_precio.text(),
            self.campo_cantidad.text()
        )
        if ok:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def actualizar_tabla(self):
        cobijas = self.service.obtener_cobijas()
        self.tabla.setRowCount(len(cobijas))
        for i, c in enumerate(cobijas):
            self.tabla.setItem(i, 0, QTableWidgetItem(c["nombre"]))
            self.tabla.setItem(i, 1, QTableWidgetItem(f"${c['precio']:.2f}"))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(c["cantidad"])))

    def limpiar_campos(self):
        self.campo_nombre.clear()
        self.campo_precio.clear()
        self.campo_cantidad.clear()