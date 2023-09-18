class Zona:
    
    def __init__(self, nombre):
        self._nombre=nombre
        self._animales=[]
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        len(self._animales)

    #metodos getters y setters para privados
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre
   
    def getAnimales(self):
        return self._animales
    
    def setAnimales(self, animales):
        self._animales=animales