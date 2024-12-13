from gestion.zona import Zona

class Zoologico():
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        
    def agregarZonas(self,n):
        self._zonas.append(n)

    def cantidadTotalAnimales(self):
        contador = 0
        for zona in this._zonas:
            contador += zona.cantidadAnimales 
        return contador
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre

    def getZona(self):
        return self._zonas
