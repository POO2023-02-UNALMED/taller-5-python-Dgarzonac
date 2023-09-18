class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas= []

    def cantidadTotalAnimales(zonas):
        _totalAnimales=0
        for i in range(len(zonas)):
            _totalAnimales+=len(zonas[i])
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    #metodos getters y setters para privados
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre=nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setNombre(self, ubicacion):
        self._ubicacion=ubicacion
    