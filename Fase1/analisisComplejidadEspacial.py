contactos = []                                                          # 1
def agregar(nombre, telefono, correo):                                  
    contacto = nombre, telefono, correo                                 # 1
    contactos.append(contacto)                                          # 1
    print(f"Contacto agregado: {contacto}")                             # 1

#funcion agregar = O(1)

def eliminar(criterio, valor):                                          
    eliminarContacto = None                                             # 1
    for contacto in contactos:                                          # n
        if contacto[criterio] == valor:                                 # 
            eliminarContacto = contacto                                 # n
            break                               
    if eliminarContacto:                                                # 1
        contactos.remove(eliminarContacto)                              # 1
        print(f"Contacto eliminado: {eliminarContacto}")                # 1
    else:
        print("Contacto no encontrado.")                                # 1

#funcion eliminar = O(n)

def buscar(criterio, valor):                                            
    for contacto in contactos:                                          # n 
        if contacto[criterio] == valor:                                 # n 
            print(f"Contacto encontrado: {contacto}")                   # n 
            return contacto                                             # n 
    print("Contacto no encontrado.")                                    # 1
    return None                                                         # 1

#funcion buscar = O(n)

def organizar():                                                        
    contactos.sort(key=lambda contacto: contacto["nombre"])             # n logn
    print("Contactos organizados:")                                     # 1
    for contacto in contactos:                                          # n
        print(contacto)                                                 # n 

#funcion organizar = O(n logn)

def menu():                                                             
    print("\nGestión de Contactos")                                     # 1
    print("1. Agregar Contacto")                                        # 1
    print("2. Eliminar Contacto")                                       # 1
    print("3. Buscar Contacto")                                         # 1
    print("4. Organizar Contactos")                                     # 1
    print("5. Salir")                                                   # 1

#funcion menu = O(1)

def busqueda():                                                         
    print("\n¿Cómo desea buscar el contacto?")                          # 1
    print("1. Nombre")                                                  # 1
    print("2. Número de teléfono")                                      # 1
    print("3. Correo")                                                  # 1
    print("4. Volver al menú anterior")                                 # 1
    opcion_busqueda = input("Seleccione una opción de búsqueda: ")      # 1    
    if opcion_busqueda == "1":                                          # 1
        return "nombre"                                                 # 1
    elif opcion_busqueda == "2":                                        # 1
        return "telefono"                                               # 1
    elif opcion_busqueda == "3":                                        # 1
        return "correo"                                                 # 1
    else:                                                               # 1
        return None                                                     # 1

#funcion busqueda = O(1)

def main():                                                             
    while True:                                                         # n 
        menu()                                                          # n
        opcion = input("Seleccione una opción: ")                       # n
        if opcion == "1":                                               # n
            nombre = input("Ingrese el nombre: ")                       # n
            telefono = input("Ingrese el teléfono: ")                   # n
            correo = input("Ingrese el correo: ")                       # n
            agregar(nombre, telefono, correo)                           # 1*n = n
        elif opcion == "2":                                             # n
            criterio = busqueda()                                           # n
            if criterio:                                                # n
                valor = input(f"Ingrese el {criterio}: ")               # n
                eliminar(criterio, valor)                               # n*n = n^2
        elif opcion == "3":                                             # n
            criterio = busqueda()                                       # n
            if criterio:                                                # n
                valor = input(f"Ingrese el {criterio}: ")               # n
                buscar(criterio, valor)                                 # n*n = n^2
        elif opcion == "4":                                             # n
            organizar()                                                 # n*n logn = n^2 logn

        elif opcion == "5":                                             # n
            print("Saliendo del programa...")                           # n
            break                                                       # n
        else:                                                           # n
            print("Opción no válida. Intente nuevamente.")              # n

if __name__ == "__main__":                                              # 1
    main()                                                              # 1

#funcion main = O(n^2 logn)