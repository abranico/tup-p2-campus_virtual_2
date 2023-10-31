from archivo import Archivo


def ingresar_como(alumnos_o_profesores, Profesor=None):
    # La funcion recibe la lista de profesores o la lista de alumnos
    # Recibe la clase Profesor cuando es necesario
    alumno_o_profesor_actual = None
    email = input("Ingrese EMAIL: ")
    password = input("Ingrese CONTRASEÑA: ")
    # Se busca si el email del alumno o profesor existe en la lista
    for alumno_o_profesor in alumnos_o_profesores:
        if email == alumno_o_profesor.email:
            alumno_o_profesor_actual = alumno_o_profesor
            break
    
    # Si el email se encuentra entonces se valida que ingrese bien la contraseña    
    if alumno_o_profesor_actual:
        if alumno_o_profesor_actual.validar_credenciales(email, password):
            # Si ingresa bien la contraseña retorna la instancia del alumno o profesor
            return alumno_o_profesor 
        else:
            print("ERROR DE INGRESO")
    else:
        # Si el email no se encuentra entonces se muestra un error o si es profesor puede crear uno
        if Profesor:
            # Se llama a una funcion para poder crear un profesor nuevo
            nuevo_profesor(email, password, Profesor, alumnos_o_profesores)
        else:
            print("Email incorrecto: Debe darse de alta en alumnado.")


def nuevo_profesor(email, password, Profesor, profesores):
    # La funcion recibe los datos y la clase para crear un nuevo Profesor
    print("Profesor no existe. Puede darse de alta ingresando un codigo.")
    codigo = input("Ingrese codigo: ")
    if codigo == "admin":
        # Si ingresa bien el codigo procede a crearse un nuevo profesor
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")                                                    
        titulo = input("Ingrese titulo: ")
        anio_egreso = int(input("Ingrese año de egreso: "))
        print("Se ha creado un nuevo profesor en el campus con la siguiente informacion:")
        print(f"Nombre: {nombre} {apellido}\nEmail: {email}\nContraseña: {password}")
        nuevo_profesor = Profesor(titulo, anio_egreso, nombre, apellido, email, password)
        profesores.append(nuevo_profesor)
    else:
        print("Codigo incorrecto.")


def ver_cursos(cursos):
    # La funcion recibe la lista de cursos y los muestra ordenado alfabeticamente
    for curso in sorted(cursos, key=lambda x: x.nombre):
        print(curso)
        

def matricularse_alumno(alumno):
    # La funcion recibe la instancia del alumno 
    # Se llama a una funcion para seleccionar el curso al que desea matricularse   
    curso_actual = seleccionar_curso_matriculacion(alumno)
    # Se valida que la funcion no haya devuelto None
    if curso_actual:
        # Se valida que el alumno no se matriculado a ese curso          
        for curso in alumno.mis_cursos:
            if curso.nombre == curso_actual.nombre:
                print("El alumno ya se encuentra matriculado a este curso.")
                # Si ya esta matriculado se sale de la funcion
                return
        
        # Si no esta matriculado entonces se le pide la clave, se valida, y se matricula                    
        matriculacion = input("Ingrese la clave de matriculacion: ")
        if matriculacion == curso_actual.contrasenia:
            alumno.matricular_en_curso(curso_actual)
            print("Alumno matriculado con exito")
        else:
            print("Clave de matriculacion incorrecta.")    

    
def seleccionar_curso_matriculacion(alumno):
    # La funcion recibe la instancia del alumno 
    carrera_actual = alumno.carrera
    # Recorre la lista de cursos de la carrera del alumno para mostrarlos
    for indice, curso in enumerate(carrera_actual.mis_cursos):
        print(f"{indice+1} - {curso.nombre}")
            
    # Se valida que haya cursos en la carrera del alumno
    if carrera_actual.get_cantidad_materias() > 0:
        seleccion = int(input("Seleccione un curso: "))
        # Se valida que ingrese uno de los cursos
        if 0 < seleccion <= carrera_actual.get_cantidad_materias():
            # Se retorna el curso seleccionado
            return carrera_actual.mis_cursos[seleccion-1]
        else:
            print("Curso inexistente.")
    else:
        print(f"No hay cursos disponibles en {carrera_actual}")

        
def desmatricularse_alumno(alumno):
    # La funcion recibe la instancia del alumno
    # Se llama a una fucion para seleccionar el curso 
    curso_actual = seleccionar_curso_de(alumno)
    # Se valida que la funcion no haya devuelto None y se desmatricula
    if curso_actual:  
        alumno.desmatricular_curso(curso_actual)
        print("Alumno Desmatriculado con exito.")      
 

def ver_cursos_de(alumno_o_profesor, esProfesor=False):
    # La funcion recibe la instancia de alumno o de profesor
    # Recibe la clase esProfesor cuando la instancia es profesor
    # Se llama a una funcion para seleccionar un curso
    curso_actual = seleccionar_curso_de(alumno_o_profesor)
    # Se valida que la funcion no haya devuelto None
    if curso_actual:
        print(f"Nombre: {curso_actual.nombre}")
        
        # Si la instancia es profesor entonces muestra mas informacion
        if esProfesor:
            print(f"Codigo: {curso_actual.codigo}")
            print(f"Contraseña: {curso_actual.contrasenia}")
            print(f"Cantidad de archivos: {len(curso_actual.archivos)}")
            opcion = int(input("¿Desea agregar un archivo adjunto? (1- Si | 2- No): "))
            if opcion == 1:
                nuevo_archivo(curso_actual)
        else:
            # Si la instancia es usuario muesta la lista de archivos del mas antiguo al mas nuevo
            for archivo in curso_actual.archivos:
                print(archivo)
               
        
def seleccionar_curso_de(alumno_profesor):
    # La funcion recibe la instancia del alumo o del profesor
    # Se valida que el objeto tenga cursos en la lista
    if len(alumno_profesor.mis_cursos) > 0:
        for indice, curso in enumerate(alumno_profesor.mis_cursos):
            print(f"{indice+1} - {curso.nombre}")

        # Se valida que ingrese uno de los cursos y lo retorna
        seleccion = int(input("Seleccione un curso: "))
        if 0 < seleccion <= len(alumno_profesor.mis_cursos):
            return alumno_profesor.mis_cursos[seleccion-1]
        else:
            print("Curso inexistente.")
    else:
        print("No hay cursos para mostrar")
           

def nuevo_archivo(curso_actual):
    # La funcion recibe la instancia del curso y luego se le agrega el nuevo archivo
    nombre = input("Ingrese nombre del archivo: ")
    formato = input("ingrese formato del archivo: ")
    nuevo_archivo = Archivo(nombre, formato)
    curso_actual.nuevo_archivo(nuevo_archivo)
    print("Archivo agregado con exito.")
    
    
def dictar_curso(cursos, Curso, profesor, carreras):
    # La funcion recibe la lista de cursos, la clase Curso, la instancia de profesor y la lista de carreras
    nombre_curso = input("Ingrese nombre del nuevo curso a dictar: ")
    # Se llama a una funcion para seleccionar una carrera
    carrera = seleccionar_carrera(carreras)
    # Se valida que la funcion no haya devuelto None
    if carrera:
        # Se instancia el curso nuevo, lo dicta y se lo agrega la lista de cursos            
        curso_nuevo = Curso(nombre_curso, carrera)
        profesor.dictar_curso(curso_nuevo)
        cursos.append(curso_nuevo)
        carrera.mis_cursos.append(curso_nuevo)
        # Se muestran los datos del curso nuevo
        print("El curso se agrego exitosamente")
        print(f"Nombre: {nombre_curso}")
        print(f"Codigo: {curso_nuevo.codigo}")
        print(f"Contraseña: {curso_nuevo.contrasenia}")

              
def seleccionar_carrera(carreras):
    # La funcion recibe la lista de carreras
    # Recorre la lista de carreras y selecciona una
    for i,carrera in enumerate(carreras):
        print(f"{i+1} - {carrera}")
    seleccion_carrera = int(input("Seleccione la carrera: "))
    if 0 < seleccion_carrera <= len(carreras):
        return carreras[seleccion_carrera-1]
    else:
        print("Carrera incorrecta")
         

