from data.database import cobijas
from models.cobija import Cobija
#unicamente touch data 
class CobijaRepository:
    #unicamente datos
    def agregar(self, cobija: Cobija):
        cobijas.append(cobija.to_dict())

    def eliminar(self, nombre: str):
        for i, c in enumerate(cobijas):
            if c["nombre"].lower() == nombre.lower():
                cobijas.pop(i)
                return True
        return False

    def editar(self, nombre: str, nuevo_precio: float, nueva_cantidad: int):
        for c in cobijas:
            if c["nombre"].lower() == nombre.lower():
                c["precio"] = nuevo_precio
                c["cantidad"] = nueva_cantidad
                return True
        return False

    def obtener_todos(self):
        return cobijas