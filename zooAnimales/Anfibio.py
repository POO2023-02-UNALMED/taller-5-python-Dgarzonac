from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    _anfibios=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.anfibios.append(self)
        Animal.totalAnimales+=1


    def crearRana(cls, nombre, edad, genero):
        ranas+=1
        return cls(nombre, edad, "selva", genero, "rojo", True)
    
    def crearSalamandra(cls, nombre, edad, genero):
        salamandras+=1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    def cantidadAnfibios(self):
        return len(self._anfibios)
    
    def movimiento():
        return "saltar"
    
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso=venenoso
    
    def getAnfibios(self):
        return self._anfibios
    
    def setAnfibios(self, anfibios):
        self._anfibios = anfibios
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel=colorPiel