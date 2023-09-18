class Animal:
    _totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero):
        totalAnimales+=1
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
    
    def movimiento():
        return "desplazarse"
    
    def totalPorTipo(self):
        return "Mamiferos: "+Animal.cantidadMamiferos()+"\n" + "Aves: "+Animal.cantidadAves()+"\n" + "Reptiles: "+Animal.cantidadReptiles()+"\n" + "Peces: "+Animal.cantidadPeces()+"\n" + "Anfibios: "+Animal.cantidadAnfibios()
    
    def __str__(self):
        if self._zona!=None:
            return "Mi nombre es " + self.nombre +  ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " +  self.getZona() + ", en el " + self.Zoologico.getNombre()
        else:
            return "Mi nombre es " + self.nombre +  ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self.genero
    
    def getTotalAnimales(self):
        return self._totalAnimales
    
    def setTotalAnimales(self, totalAnimales):
        self._totalAnimales=totalAnimales
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self):
        self._nombre=nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad=edad
    
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat=habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero=genero
    
    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona=zona