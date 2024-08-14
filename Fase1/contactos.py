contactos = []

def agregar(nombre, telefono, correo):
    contacto = {nombre, telefono, correo}
    contactos.append(contacto)
    print("Contacto agregado con éxito.")

def eliminar(nombre):
    eliminarContacto = None
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            eliminarContacto = contacto
            break
    if eliminarContacto:
        contactos.remove(eliminarContacto)
        print("Contacto eliminado con éxito.")
    else:
        print("Contacto no encontrado.")

def buscar(nombre):
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            print(f"Información del contacto {nombre}:")
            print(f" Nombre: {contacto['nombre']}")
            print(f" Teléfono: {contacto['telefono']}")
            print(f" Correo: {contacto['correo']}")
            return
    print("Contacto no encontrado.")

def organizar():
    contactos.sort(key=lambda contacto: contacto["nombre"])
    print("Lista de contactos organizada:")
    for contacto in contactos:
        print(f" - {contacto['nombre']}")

def ejecutar_comando(comando):
    partes = comando.split()
    accion = partes[0].upper()
    if accion == "AGREGAR" and len(partes) == 4:
        nombre = partes[1]
        telefono = partes[2]
        correo = partes[3]
        agregar(nombre, telefono, correo)
    elif accion == "ELIMINAR" and len(partes) == 2:
        nombre = partes[1]
        eliminar(nombre)
    elif accion == "BUSCAR" and len(partes) == 2:
        nombre = partes[1]
        buscar(nombre)
    elif accion == "ORGANIZAR":
        organizar()
    elif accion == "SALIR":
        exit()
    else:
        print("Comando no válido o parámetros incorrectos.")

while True:
    comando = input("")
    ejecutar_comando(comando)
