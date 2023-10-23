from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    def dictar_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def anio_egreso(self):
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso):
        self.__anio_egreso = nuevo_anio_egreso

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, nueva_lista):
        self.__mis_cursos = nueva_lista
