from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera


carreras = [
    Carrera("Tecnicatura Universitaria en Programación", 2, [], []),
    Carrera("Ingenieria en Sistemas", 5, [], [])
    
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
               "facundo@gmail.com", "contrasenia5"),
    Estudiante(6, 2017, carreras[1], "Ignacio", "Quiroga",
               "ignacio@gmail.com", "contrasenia6"),
]


cursos = [
    Curso( "Ingles I", carreras[0], "a4e52"),
    Curso( "Ingles II", carreras[0], "Ds3y2"),
    Curso( "Quimica", carreras[1], "rB266"),
    Curso( "Laboratorio I", carreras[0], "9Lom2"),
    Curso( "Laboratorio II", carreras[0], "hH2ml"),
    Curso( "Algoritmos", carreras[1], "rB266"),
    Curso( "Programación I", carreras[0], "mL22s"),
    Curso( "Programación II", carreras[0], "912Md"),
    Curso( "Fisica", carreras[1], "rB266")
    

]

for estudiante in estudiantes:
        for carrera in carreras:
            if estudiante.carrera == carrera:
                carrera.mis_estudiantes.append(estudiante)

def cargar_cursos_a_carreras():
    # Limpio la lista de cursos de la carrera para que no se dupliquen
    for carrera in carreras:
        carrera.mis_cursos = []
    
    # Cargo los cursos dentro de la carrera                  
    for curso in cursos:
        for carrera in carreras:
            if curso.carrera == carrera:
                carrera.mis_cursos.append(curso)

cargar_cursos_a_carreras()

