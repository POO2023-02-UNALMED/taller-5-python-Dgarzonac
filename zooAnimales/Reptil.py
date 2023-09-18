from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas=0
    serpientes=0
    _reptiles=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._reptiles.append(self)
        Animal.totalAnimales+=1
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas+=1
        return cls(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes+=1
        return cls(nombre, edad, "jungla", genero, "blanco", 1)
    
    def movimiento():
        return "reptar"

    def cantidadReptiles(self):
        return len(self._reptiles)
    
    def getReptiles(self):
        return self._reptiles
    
    def setReptiles(self, reptiles):
        self._reptiles=reptiles

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola=largoCola
    
    def getColorEscamas(self):
       return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas
