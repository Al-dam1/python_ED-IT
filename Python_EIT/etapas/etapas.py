usuario = 'admin'
contraseña = 'uni123'
listaAlumnos = []

IngresNombre = input('Ingresa el usuario: ')
IngreseContraseña = input('Ingresa la contraseña: ')

if (IngresNombre == usuario and IngreseContraseña == contraseña):
    while True:
        print('Ingrese el número de la operación que desea ejecutar: ')
        print('1 - Añadir un alumno a la lista.') 
        print('2 - Ver la lista de alumnos.') 
        print('3 - Salir.')
        opcion = int(input('ingresa una opcion: '))
        if opcion == 1:
            IngresoAlumno = input('Ingrese el nombre: ')
            cantidadCursos = int(input('ingresa la cantidad de cursos: '))
            alumno = f'El alumno {IngresoAlumno}, tiene un total de {cantidadCursos} cursos'
            listaAlumnos.append(alumno)
        elif opcion == 2:
            print('Lista de alumnos:')
            for alumno in listaAlumnos:
                print(alumno)
        elif opcion == 3:
            print('¡Gracias por utilizar el programa!')
            break
        else:
            print('La opción ingresada no es correcta, vuelva a intentarlo.')

else:
    print('Usuario/o contraseña no encontrado')



