from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    aves=[]
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Ave.aves.append(self)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones+=1
        return cls(nombre, edad, "montanas", genero, "cafe glorioso", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Ave.aguilas+=1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo", False)
    
   
    def movimiento():
        return "volar"

    def getColorPlumas(self):
        return self._colorPlumas
    
    def cantidadAves(self):
        return len(self.aves)

    def getAves(self):
        return self.aves
    
    def setAves(self, aves):
        self.aves=aves
