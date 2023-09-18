from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    _peces=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._peces.append(self)
        Animal.totalAnimales+=1
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones+=1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos+=1
        return cls(nombre, edad, "oceano", genero, "gris", 6)
    
    def movimiento():
        return "nadar"

    def cantidadPeces(self):
        return len(self._peces)
    
    def getPeces(self):
        return self._peces
    
    def setPeces(self, peces):
        self._peces=peces

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantiadaAletas=cantidadAletas
    
    def getColorEscamas(self):
       return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas
