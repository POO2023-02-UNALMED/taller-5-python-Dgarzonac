from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    anfibios=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.anfibios.append(self)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Anfibio.ranas+=1
        return cls(nombre, edad, "selva", genero, "rojo", True)
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Anfibio.salamandras+=1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.anfibios)
    
    def movimiento():
        return "saltar"
    
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso=venenoso
    
    def getAnfibios(self):
        return self.anfibios
    
    def setAnfibios(self, anfibios):
        self.anfibios = anfibios
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel=colorPiel
    def toString(self):
        return self.__str__()
    