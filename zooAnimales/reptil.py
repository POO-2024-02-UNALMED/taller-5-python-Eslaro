class Reptil(Animal):
    _listado = []
    iguanas = 0 
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        cls._listado.append(self)
    
    def getColorEscamas(self):
        return self._colorEscamas
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def getLargoCola():
        return self._largoCola
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpientes += 1
        return Reptil(nombre, edad, "humedal", genero, "blanco", 1 )
    def movimiento(self):
        return "reptar"