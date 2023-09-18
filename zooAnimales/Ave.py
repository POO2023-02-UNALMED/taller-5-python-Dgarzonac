import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    _aves=[]
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Ave._aves.append(self)
        Animal.totalAnimales+=1
    def crearHalcon(cls, nombre, edad, genero):
        halcones+=1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso", True)
    def crearSalamandra(cls, nombre, edad, genero):
        aguilas+=1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo", False)
    
   
    def movimiento():
        return "volar"

    def getColorPlumas(self):
        return self._colorPlumas
    
    def cantidadAves(self):
        return len(self._aves)

    def getAves(self):
        return self._aves
    
    def setAves(self, aves):
        self._aves=aves
