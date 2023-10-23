from abc import ABC, abstractclassmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} {self.apellido} Email: {self.email}"

    def validar_credenciales(self, email, contrasenia) -> bool:
        if self._email == email and self._contrasenia == contrasenia:
            return True
        else:
            return False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nuevo_contrasenia):
        self._contrasenia = nuevo_contrasenia
