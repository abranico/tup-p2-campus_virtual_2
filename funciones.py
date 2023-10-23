
def ingresar_como(alumnos_o_profesores, Profesor=None):
    alumno_o_profesor_actual = None
    email = input("Ingrese EMAIL: ")
    password = input("Ingrese CONTRASEÑA: ")
    for alumno_o_profesor in alumnos_o_profesores:
        if email == alumno_o_profesor.email:
            alumno_o_profesor_actual = alumno_o_profesor
            break
    if alumno_o_profesor_actual:
        if alumno_o_profesor_actual.validar_credenciales(email, password):
            return alumno_o_profesor
        else:
            print("ERROR DE INGRESO")
    else:
        if Profesor:
            print("Profesor no existe. Puede darse de alta ingresando un codigo.")
            codigo = input("Ingrese codigo: ")
            if codigo == "admin":
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                titulo = input("Ingrese titulo: ")
                anio_egreso = int(input("Ingrese año de egreso: "))
                nuevo_profesor = Profesor(titulo, anio_egreso, nombre, apellido, email, password)
                alumnos_o_profesores.append(nuevo_profesor)
            else:
                print("Codigo incorrecto.")
        else:
            print("Email incorrecto: Debe darse de alta en alumnado.")


def ver_cursos(cursos):
    for curso in cursos:
        print(
            f"Materia: {curso} Carrera: Tecnicatura Universitaria en Programación")


def nuevo_curso(cursos, Curso, profesor):
    nombre_curso = input("Ingrese nombre del curso nuevo: ")
    curso_nuevo = Curso(nombre_curso)
    cursos.append(curso_nuevo)
    profesor.dictar_curso(curso_nuevo)
    print("El curso se agrego exitosamente.")
    print(f"Nombre: {nombre_curso}")
    print(f"Contraseña: {curso_nuevo.contrasenia}")


def matricularse_alumno(cursos, alumno):
    encontrado = False
    for indice, curso in enumerate(cursos):
        print(f"{indice+1} - {curso}")

    seleccion = int(input("Seleccione un curso: "))
    if seleccion > 0 and seleccion <= len(cursos):
        for curso in alumno.mis_cursos:
            if curso.nombre == cursos[seleccion-1].nombre:
                print("El alumno ya se encuentra matriculado.")
                encontrado = True
        if not encontrado:
            matriculacion = input("Ingrese la clave de matriculacion: ")
            if matriculacion == cursos[seleccion-1].contrasenia:
                alumno.matricular_en_curso(cursos[seleccion-1])
            else:
                print("Clave de matriculacion incorrecta.")

    else:
        print("Curso inexistente.")


def mostar_cursos_de(alumno_o_profesor, esProfesor=False):
    if len(alumno_o_profesor.mis_cursos) > 0:
        for indice, curso in enumerate(alumno_o_profesor.mis_cursos):
            print(f"{indice+1} - {curso}")

        seleccion = int(input("Seleccione un curso: "))
        if seleccion > 0 and seleccion <= len(alumno_o_profesor.mis_cursos):
            for curso in alumno_o_profesor.mis_cursos:
                if curso.nombre == alumno_o_profesor.mis_cursos[seleccion-1].nombre:
                    print(f"Nombre: {curso.nombre}")
                    if esProfesor:
                        print(f"Contraseña: {curso.contrasenia}")

        else:
            print("Curso inexistente.")
    else:
        print("No hay cursos para mostrar")
