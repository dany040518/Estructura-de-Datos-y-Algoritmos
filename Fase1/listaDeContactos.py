contactos = []

def agregar(nombre, telefono, correo):
    contacto = nombre, telefono, correo
    contactos.append(contacto)
    print(f"Contacto agregado: {contacto}")

def eliminar(criterio, valor):
    eliminarContacto = None
    for contacto in contactos:
        if contacto[criterio] == valor:
            eliminarContacto = contacto
            break
    if eliminarContacto:
        contactos.remove(eliminarContacto)
        print(f"Contacto eliminado: {eliminarContacto}")
    else:
        print("Contacto no encontrado.")

def buscar(criterio, valor):
    for contacto in contactos:
        if contacto[criterio] == valor:
            print(f"Contacto encontrado: {contacto}")
            return contacto
    print("Contacto no encontrado.")
    return None

def organizar():
    contactos.sort(key=lambda contacto: contacto["nombre"])
    print("Contactos organizados:")
    for contacto in contactos:
        print(contacto)

def menu():
    print("\nGestión de Contactos")
    print("1. Agregar Contacto")
    print("2. Eliminar Contacto")
    print("3. Buscar Contacto")
    print("4. Organizar Contactos")
    print("5. Salir")

def busqueda():
    print("\n¿Cómo desea buscar el contacto?")
    print("1. Nombre")
    print("2. Número de teléfono")
    print("3. Correo")
    print("4. Volver al menú anterior")
    opcion_busqueda = input("Seleccione una opción de búsqueda: ")
    if opcion_busqueda == "1":
        return "nombre"
    elif opcion_busqueda == "2":
        return "telefono"
    elif opcion_busqueda == "3":
        return "correo"
    else:
        return None

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo: ")
            agregar(nombre, telefono, correo)

        elif opcion == "2":
            criterio = busqueda()
            if criterio:
                valor = input(f"Ingrese el {criterio}: ")
                eliminar(criterio, valor)

        elif opcion == "3":
            criterio = busqueda()
            if criterio:
                valor = input(f"Ingrese el {criterio}: ")
                buscar(criterio, valor)

        elif opcion == "4":
            organizar()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()