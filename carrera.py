

class Carrera:
    def __init__(self, nombre: str, cant_anios: int, cursos : list, estudiantes: list) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__mis_cursos = cursos
        self.__mis_estudiantes = estudiantes

    def __str__(self) -> str:
        return self.nombre

    def get_cantidad_materias(self) -> int:
        return len(self.mis_cursos)

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
        
    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    @mis_cursos.setter
    def mis_cursos(self, nueva_lista):
        self.__mis_cursos = nueva_lista
        
    @property
    def mis_estudiantes(self):
        return self.__mis_estudiantes
    
    @mis_estudiantes.setter
    def mis_estudiantes(self, nueva_lista):
        self.__mis_estudiantes = nueva_lista
