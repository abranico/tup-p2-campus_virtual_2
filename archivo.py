from datetime import date


class Archivo:
    def __init__(self, nombre:str, formato:str, fecha:date=date.today() ) -> None:
        self.__nombre=nombre
        self.__fecha=fecha
        self.__formato=formato
    
    def __str__(self) -> str:
        return self.nombre+"."+self.formato

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevoNombre):
        self.__nombre=nuevoNombre
        
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nuevaFecha):
        self.__fecha=nuevaFecha
        
    @property
    def formato(self):
        return self.__formato
    
    @formato.setter
    def formato(self, nuevoFormato):
        self.__formato=nuevoFormato
    