
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
                email = input("Ingrese email: ")
                password = input("Ingrese contraseña: ")
                if password != input("Vuelva a ingresar la contraseña: "):
                    print("Las contraseñas no coinciden, vuelve a intentarlo")
                    return 
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
    for curso in sorted(cursos, key=lambda x: x.nombre):
        print(curso)


def nuevo_curso(cursos, Curso, profesor, carreras):
    nombre_curso = input("Ingrese nombre del curso nuevo: ")
    for i,carrera in enumerate(carreras):
        print(f"{i+1} - {carrera}")
    seleccion_carrera = int(input("Seleccione la carrera: "))
    if seleccion_carrera > 0 and seleccion_carrera <= len(carreras):
        curso_nuevo = Curso(nombre_curso, carreras[seleccion_carrera-1])
        cursos.append(curso_nuevo)
        profesor.dictar_curso(curso_nuevo)
        print("El curso se agrego exitosamente.")
        print(f"Nombre: {nombre_curso}")
        print(f"Codigo: {curso_nuevo.codigo}")
        print(f"Contraseña: {curso_nuevo.contrasenia}")
    else:
        print("Carrera incorrecta")


def matricularse_alumno(cursos, alumno):
    encontrado = False
    cant_cursos_disponibles = 0
    for indice, curso in enumerate(cursos):
        if curso.carrera == alumno.carrera:
            print(f"{indice+1} - {curso.nombre}")
            cant_cursos_disponibles+=1
    if cant_cursos_disponibles == 0:
        print("No hay cursos disponibles para este alumno.")
        return

    seleccion = int(input("Seleccione un curso: "))
    if seleccion > 0 and seleccion <= cant_cursos_disponibles:
        if cursos[seleccion-1].carrera == alumno.carrera:
            for curso in alumno.mis_cursos:
                if curso.nombre == cursos[seleccion-1].nombre:
                    print("El alumno ya se encuentra matriculado a este curso.")
                    encontrado = True
            if not encontrado:
                matriculacion = input("Ingrese la clave de matriculacion: ")
                if matriculacion == cursos[seleccion-1].contrasenia:
                    alumno.matricular_en_curso(cursos[seleccion-1])
                    print("Alumno matriculado con exito")
                else:
                    print("Clave de matriculacion incorrecta.")
        else:
            print("Este curso es exclusivo para estudiantes de la carrera correspondiente")

    else:
        print("Curso inexistente.")


def mostar_cursos_de(alumno_o_profesor, esProfesor=False):
    if len(alumno_o_profesor.mis_cursos) > 0:
        for indice, curso in enumerate(alumno_o_profesor.mis_cursos):
            print(f"{indice+1} - {curso.nombre}")

        seleccion = int(input("Seleccione un curso: "))
        if seleccion > 0 and seleccion <= len(alumno_o_profesor.mis_cursos):
            for curso in alumno_o_profesor.mis_cursos:
                if curso.nombre == alumno_o_profesor.mis_cursos[seleccion-1].nombre:
                    print(f"Nombre: {curso.nombre}")
                    for archivo in sorted(curso.archivos, key=lambda x:x.fecha):
                        print(archivo)
                    if esProfesor:
                        print(f"Contraseña: {curso.contrasenia}")
                        print(f"Cantidad de archivos: {len(curso.archivos)}")                        
        else:
            print("Curso inexistente.")
    else:
        print("No hay cursos para mostrar")

def desmatricularse_alumno(alumno):
    if len(alumno.mis_cursos) > 0:
        for indice, curso in enumerate(alumno.mis_cursos):
            print(f"{indice+1} - {curso.nombre}")

        seleccion = int(input("Seleccione un curso: "))
        if seleccion > 0 and seleccion <= len(alumno.mis_cursos):
            for curso in alumno.mis_cursos:
                if curso.nombre == alumno.mis_cursos[seleccion-1].nombre:
                    alumno.desmatricular_curso(curso)
                    print("Alumno Desmatriculado con exito.")
        else:
            print("Curso inexistente.")
    else:
        print("Este alumno no esta matriculado a ningun curso")

