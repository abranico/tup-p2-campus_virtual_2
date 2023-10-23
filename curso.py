import random
import string
from carrera import Carrera
from archivo import Archivo


class Curso:
    __prox_cod: int = 0

    def __init__(self, codigo: int, nombre: str, carrera: Carrera, contrasenia_matriculacion: str = None):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__carrera = carrera
        self.__archivos = []

        self.__contrasenia_matriculacion = Curso.__generar_contrasenia(
        ) if contrasenia_matriculacion is None else contrasenia_matriculacion

    def __str__(self) -> str:
        return f"Materia: {self.nombre} Carrera: {self.carrera}"

    def nuevo_archivo(self, archivo: Archivo):
        pass

    @classmethod
    def __generar_contrasenia(cls) -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

    @property
    def archivos(self):
        return self.__archivos

    @carrera.setter
    def archivos(self, nueva_archivos):
        self.__archivos = nueva_archivos

    @property
    def contrasenia(self):
        return self.__contrasenia_matriculacion

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia_matriculacion = nueva_contrasenia
