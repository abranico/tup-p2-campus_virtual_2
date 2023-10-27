from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from funciones import *

carreras = [
    Carrera("Tecnicatura Universitaria en Programación", 2),
    Carrera("Ingenieria en Sistemas", 5)
    
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
    Curso( "Ingles I", carreras[0], "a4e52"),
    Curso( "Ingles II", carreras[0], "Ds3y2"),
    Curso( "Laboratorio I", carreras[0], "9Lom2"),
    Curso( "Laboratorio II", carreras[0], "hH2ml"),
    Curso( "Programación I", carreras[0], "mL22s"),
    Curso( "Programación II", carreras[0], "912Md"),
    Curso( "Fisica", carreras[1], "rB266")
    

]


def menu_principal():
    print("---------- MENU ----------")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    return int(input("Ingrese una opcion: "))


def menu_alumno():
    print("---------- MENU ALUMNO ----------")
    print("1. Matricularse a un curso")
    print("2. Desmatricularse a un curso")
    print("3. Ver curso")
    print("4. Volver al menu principal")
    return int(input("Ingrese una opcion: "))


def menu_profesor():
    print("---------- MENU PROFESOR ----------")
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
                    desmatricularse_alumno(alumno)
                elif opcion == 3:
                    mostar_cursos_de(alumno)
                elif opcion == 4:
                    break
                else:
                    print("Opcion incorrecta")
    elif opcion == 2:
        profesor = ingresar_como(profesores, Profesor)
        if profesor:
            while True:
                opcion = menu_profesor()
                if opcion == 1:
                    nuevo_curso(cursos, Curso, profesor, carreras)
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
