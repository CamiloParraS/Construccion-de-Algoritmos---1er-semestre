from src.ListaDeContactos import ListaDeContactos

class Menu:
    
    def __init__(self):
        self.__miListaDeContactos = ListaDeContactos()
    
    def MenuPrincipal(self):
        salir = False

        while not salir:
            print("----------------------------------------------------------------")
            print("Lista de contactos")
            print("----------------------------------------------------------------")
            print("1. Agregar contacto")
            print("2. Dar todos los contactos")
            print("3. Buscar contacto por palabra clave")
            print("4. Buscar contacto")
            print("5. Eliminar contacto")
            print("6. Modificar contacto")
            print("0. Salir")
            print("----------------------------------------------------------------")
            
            try:
                op = int(input('Digite una opción: '))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if op == 1:
                datos = self.SolicitarDatosCompletos()
                print(('no agregado', 'agregado con exito')[self.__miListaDeContactos.agregarContacto(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])])
                
            elif op == 2:
                contactos = self.__miListaDeContactos.darTodosLosContactos()
                print('Contactos: ', contactos if contactos else 'No hay contactos registrados')
                
            elif op == 3:
                print(self.__miListaDeContactos.buscarContactosPalabraClave(input('Digite palabra clave: ')))
                
            elif op == 4:
                contacto=self.__miListaDeContactos.buscarContacto(input('Digite nombre: '), input('Digite apellido: '))
                
                print("Datos:", contacto.darNombre(), contacto.darApellido())
                print("Direccion:", contacto.darDireccion())
                print("correo electronico", contacto.darCorreo())
                print("Numeros telefonicos:")
                print(contacto.darTelefonos())
                print("Palabras claves:")
                print(contacto.darPalabras())
                    
            elif op == 5:
                nombre = input("Digite nombre: ")
                apellido = input("Digite apellido: ")
                eliminado = self.__miListaDeContactos.eliminarContacto(nombre, apellido)
                print("Contacto eliminado" if eliminado else "El contacto no existía")
                
            elif op == 6:
                print("Modificar Contacto")
                nombre = input("Digite el nombre del contacto a modificar: ")
                apellido = input("Digite el apellido del contacto a modificar: ")
                contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
                
                if not contacto:
                    print("El contacto no existe.")
                else:
                    print(f"Contacto encontrado: {contacto.darNombre()} {contacto.darApellido()}")
                    
                    nueva_direccion = input("Nueva dirección (dejar vacío para no modificar): ") or contacto.darDireccion()
                    nuevo_correo = input("Nuevo correo (dejar vacío para no modificar): ") or contacto.darCorreo()
                    nuevos_telefonos = self.AgregarTelefonos() if input("¿Modificar teléfonos? (s/n): ").lower() == 's' else contacto.darTelefonos()
                    nuevas_palabras = self.AgregarPalabras() if input("¿Modificar palabras clave? (s/n): ").lower() == 's' else contacto.darPalabras()
                    
                    modificado = self.__miListaDeContactos.modificarContacto(
                        nombre, apellido, nueva_direccion, nuevo_correo, nuevos_telefonos, nuevas_palabras
                    )
                    print("Contacto modificado con éxito" if modificado else "No se pudo modificar el contacto")
            
            elif op == 0:
                salir = True
                
            else:
                print("Opción inválida. Intente de nuevo.")

        print("Adiós.")
    
    def SolicitarDatosCompletos(self):
        nombre = input('Digite nombre: ')
        apellido = input('Digite apellido: ')
        direccion = input('Digite dirección: ')
        correo = input('Digite correo: ')
        telefonos = self.AgregarTelefonos()
        palabras = self.AgregarPalabras()
        return [nombre, apellido, direccion, correo, telefonos, palabras]
        
    def AgregarTelefonos(self):
        salir = False
        telefonos = []
        
        while not salir:
            
            telefono=input('Digite telefono: ')
            
            if telefono.isdigit():
                telefonos.append(telefono)
            else: 
                print('No es un numero de telefono')

            op = int(input('Desea agregar otro telefono si=1,no=2: '))
            if op == 2:
                salir = True
        
        return telefonos
    
    def AgregarPalabras(self):

        palabras = []
        print('Abreviatura de contacto')
        nombre=input('Digite nombre: ')
        apellido=input('Digite apellido: ')
        
        palabras.append(nombre)
        palabras.append(apellido)

        
        return palabras

menu = Menu()
print(menu.MenuPrincipal())