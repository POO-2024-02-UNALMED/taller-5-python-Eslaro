
class Zona():
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self,n):
        self._animales.append(n)

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo