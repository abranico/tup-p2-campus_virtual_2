from funciones import *
from datos import *
import os

def menu_principal():
    print("\n---------- MENU ----------")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    return int(input("Ingrese una opcion: "))


def menu_alumno():
    print("\n---------- MENU ALUMNO ----------")
    print("1. Matricularse a un curso")
    print("2. Desmatricularse a un curso")
    print("3. Ver cursos")
    print("4. Volver al menu principal")
    return int(input("Ingrese una opcion: "))


def menu_profesor():
    print("\n---------- MENU PROFESOR ----------")
    print("1. Dictar curso")
    print("2. Ver cursos")
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
                    os.system('cls')
                    matricularse_alumno(alumno)
                elif opcion == 2:
                    os.system('cls')
                    desmatricularse_alumno(alumno)
                elif opcion == 3:
                    os.system('cls')
                    ver_cursos_de(alumno)
                elif opcion == 4:
                    os.system('cls')
                    break
                else:
                    print("Opcion incorrecta")
    elif opcion == 2:
        profesor = ingresar_como(profesores, Profesor)
        if profesor:
            while True:
                opcion = menu_profesor()
                if opcion == 1:
                    os.system('cls')
                    dictar_curso(cursos, Curso, profesor, carreras)
                elif opcion == 2:
                    os.system('cls')
                    ver_cursos_de(profesor, True)
                elif opcion == 3:
                    os.system('cls')
                    break
    elif opcion == 3:
        os.system('cls')
        ver_cursos(cursos)
    elif opcion == 4:
        os.system('cls')
        print("Gracias por usar nuestro sistema.")
        break
    else:
        print("Opcion incorrecta")
