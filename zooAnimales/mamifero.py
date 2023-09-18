import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    _mamiferos=[]
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super.__init__(nombre, edad, habitat, genero)
        self._patas=patas
        self._pelaje=pelaje
        Mamifero._aves.append(self)
        Animal.totalAnimales+=1
    
    def crearCaballo(cls, nombre, edad, genero):
        halcones+=1
        return cls(nombre, edad, "pradera", genero, True, 4)
    def crearLeon(cls, nombre, edad, genero):
        leones+=1
        return cls(nombre, edad, "selva", genero, True, 4)
    
    def movimiento():
        return "desplazarse"

    def cantidadMamiferos(self):
        return len(self._mamiferos)
    
    def getMamiferos(self):
        return self._mamiferos
    
    def setMamiferos(self, mamiferos):
        self._mamiferos=mamiferos

    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas=patas

    def isPelaje(self):
        return self._pelaje;

    def setPelaje(self, pelaje):
        self._pelaje=pelaje
