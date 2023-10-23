

class Carrera:
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    def __str__(self) -> str:
        return self.nombre

    def get_cantidad_materias(self) -> int:
        pass

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def cant_anios(self):
        return self.__cant_anios

    @cant_anios.setter
    def cant_anios(self, nuevaCantidad):
        self.__cant_anios = nuevaCantidad
