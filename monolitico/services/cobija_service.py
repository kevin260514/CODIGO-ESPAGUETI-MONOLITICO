from repositories.cobija_repository import CobijaRepository
from models.cobija import Cobija

class CobijaService:

    def __init__(self):
        self.repository = CobijaRepository()

    def agregar_cobija(self, nombre, precio, cantidad):
        if not nombre or not precio or not cantidad:
            return False, "Rellena todos los campos"
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except:
            return False, "Precio o cantidad inválidos"

        cobija = Cobija(nombre, precio, cantidad)
        self.repository.agregar(cobija)
        return True, f"Cobija '{nombre}' agregada correctamente"

    def eliminar_cobija(self, nombre):
        if not nombre:
            return False, "Escribe el nombre a eliminar"
        encontrado = self.repository.eliminar(nombre)
        if encontrado:
            return True, f"Cobija '{nombre}' eliminada correctamente"
        return False, f"No se encontró '{nombre}'"

    def editar_cobija(self, nombre, nuevo_precio, nueva_cantidad):
        if not nombre:
            return False, "Escribe el nombre de la cobija a editar"
        if not nuevo_precio or not nueva_cantidad:
            return False, "Escribe el nuevo precio y cantidad"
        try:
            nuevo_precio = float(nuevo_precio)
            nueva_cantidad = int(nueva_cantidad)
        except:
            return False, "Precio o cantidad inválidos"

        encontrado = self.repository.editar(nombre, nuevo_precio, nueva_cantidad)
        if encontrado:
            return True, f"Cobija '{nombre}' actualizada correctamente"
        return False, f"No se encontró '{nombre}'"

    def obtener_cobijas(self):
        return self.repository.obtener_todos()