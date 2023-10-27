from usuario import Usuario
from curso import Curso
from carrera import Carrera


class Estudiante(Usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int, carrera: Carrera, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__carrera = carrera
        self.__mis_cursos = []

    def matricular_en_curso(self, curso: Curso):
        self.mis_cursos.append(curso)

    def desmatricular_curso(self, curso: Curso):
        self.mis_cursos.remove(curso)

    @property
    def legajo(self) -> list:
        return self.__legajo

    @legajo.setter
    def legajo(self, nueva_legajo):
        self.__legajo = nueva_legajo

    @property
    def anio_inscripcion_carrera(self) -> list:
        return self.__anio_inscripcion_carrera

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio):
        self.__anio_inscripcion_carrera = nuevo_anio

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, nueva_lista):
        self.__mis_cursos = nueva_lista
        
    @property
    def carrera(self) -> list:
        return self.__carrera
