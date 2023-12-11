print ("Directorio General")
directorio = []
#Directorio entre corchetes para identificar el valor a poner en la variable
 
def agregar_persona():
    clave = input("Ingrese la clave: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    departamento = input("Ingrese el departamento: ")
    
    persona = {
        'Clave': clave,
        'Nombre': nombre,
        'Dirección': direccion,
        'Teléfono': telefono,
        'Departamento': departamento
    }
    
def persona():
    clave = input("Ingrese la clave: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    departamento = input("Ingrese el departamento: ")
    persona = {
        'Clave': clave,
        'Nombre': nombre,
        'Dirección': direccion,
        'Teléfono': telefono,
        'Departamento': departamento
    }
    
    
    
    directorio.append(persona)
    print("Persona agregada al directorio.")
 
def buscar_persona():
    Sets = ("Clave", "Nombre", "Dirección", "Teléfono", "Departamento")
    print("Elija la opción de búsqueda:")
    for i, Set in enumerate(Sets, 1):
        print(f"{i}. {Set}")
    
    opcion = int(input("Seleccione el número de opción: "))
    
    if 1 <= opcion <= len(Sets):
        #uso la funcion len para devolver un valor entero que indica la cantidad de caracteres en la cadena de entrada.
        opcion_seleccionada = Sets[opcion - 1]
        valor = input(f"Ingrese el {opcion_seleccionada} que desea buscar: ")
        
        resultados = [persona for persona in directorio if persona[opcion_seleccionada] == valor]
        
        if resultados:
            print("Resultados de la búsqueda:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron resultados para la búsqueda.")
    else:
        print("Opción no válida. Por favor, seleccione un número de opción válido.")
 

while True:
    print("\n1. Agregar persona al directorio")
    print("2. Buscar persona en el directorio")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_persona()
    elif opcion == '2':
        buscar_persona()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
    directorio.append(agregar_persona)
    #aca yo utilize append para agregar un valor al apatartaeo (persona)
    print("Persona agregada al directorio.")
 
def buscar_persona():
    opcion = input("Elija la opción de búsqueda (clave, nombre, dirección, teléfono, departamento): ")    
    valor = input(f"Ingrese {opcion} de busqueda: ")
 
    resultados = [persona for persona in directorio if persona[opcion] == valor]
 
    if resultados:
        print("Resultados de la búsqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron resultados para la búsqueda.")
 
while True:
    print("1. Agregar personal en el directorio")
    print("2. Buscar a personal dentro del directorio")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_persona()
    elif opcion == '2':
        buscar_persona()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")