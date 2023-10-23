from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from funciones import *

carreras = [
    Carrera("Tecnicatura Universitaria en Programación", 2)
]

profesores = [
    Profesor("Ingenieria en Sistemas", 2005, "Carlos",
             "González", "carlos@gmail.com", "contrasenia1"),
    Profesor("Ingenieria en Sistemas", 2010, "Laura",
             "Martínez", "laura@gmail.com", "contrasenia2"),
    Profesor("Ingenieria en Sistemas", 2008, "Eduardo",
             "López", "eduardo@gmail.com", "contrasenia3"),
    Profesor("Profesorado de Ingles", 2003, "Ana",
             "Pérez", "ana@gmail.com", "contrasenia4"),
    Profesor("Profesorado de Ingles", 2012, "Javier",
             "Rodríguez", "javier@gmail.com", "contrasenia5")
]

estudiantes = [
    Estudiante(1, 2022, carreras[0], "Mariano", "Gómez",
               "mariano@gmail.com", "contrasenia1"),
    Estudiante(2, 2021, carreras[0], "Sofía", "Martínez",
               "sofia@gmail.com", "contrasenia2"),
    Estudiante(3, 2020, carreras[0], "Juan",
               "Pérez", "juan@gmail.com", "contrasenia3"),
    Estudiante(4, 2019, carreras[0], "Valentina", "Rodríguez",
               "valentina@gmail.com", "contrasenia4"),
    Estudiante(5, 2018, carreras[0], "Facundo", "López",
               "facundo@gmail.com", "contrasenia5")
]

cursos = [
    Curso(0, "Ingles I", "a4e52", carreras[0]),
    Curso(1, "Ingles II", "Ds3y2", carreras[0]),
    Curso(2, "Laboratorio I", "9Lom2", carreras[0]),
    Curso(3, "Laboratorio II", "hH2ml", carreras[0]),
    Curso(4, "Programación I", "mL22s", carreras[0]),
    Curso(5, "Programación II", "912Md", carreras[0])
]


def menu_principal():
    print("---------- MENU ----------")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    return int(input("Ingrese una opcion: "))


def menu_alumno():
    print("---------- MENU ----------")
    print("1. Matricularse a un curso")
    print("2. Ver curso")
    print("3. Volver al menú principal")
    return int(input("Ingrese una opcion: "))


def menu_profesor():
    print("---------- MENU ----------")
    print("1. Dictar curso")
    print("2. Ver curso")
    print("3. Volver al menu principal")
    return int(input("Ingrese una opcion: "))


while True:
    opcion = menu_principal()
    if opcion == 1:
        alumno = ingresar_como(estudiantes)
        if alumno:
            while True:
                opcion = menu_alumno()
                if opcion == 1:
                    matricularse_alumno(cursos, alumno)
                elif opcion == 2:
                    mostar_cursos_de(alumno)
                elif opcion == 3:
                    break
                else:
                    print("Opcion incorrecta")
    elif opcion == 2:
        profesor = ingresar_como(profesores, Profesor)
        if profesor:
            while True:
                opcion = menu_profesor()
                if opcion == 1:
                    nuevo_curso(cursos, Curso, profesor)
                elif opcion == 2:
                    mostar_cursos_de(profesor, True)
                elif opcion == 3:
                    break
    elif opcion == 3:
        ver_cursos(cursos)
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
