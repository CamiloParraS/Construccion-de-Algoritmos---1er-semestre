from src.ListaDeContactos import ListaDeContactos

class Menu:
    
    def __init__(self):
        self.__miListaDeContactos = ListaDeContactos();
    
    def MenuPrincipal(self):
        salir = False

        while not salir:
            print ("----------------------------------------------------------------")
            print ("Lista de contactos")
            print ("----------------------------------------------------------------")
            print ("1. Agregar contacto")
            print ("2. Dar todos los contactos")
            print ("3. Buscar contacto por palabra clave")
            print ("4. Buscar contacto")
            print ("5. Eliminar contacto")
            print ("6. Modificar contacto")
            print ("0. Salir")
            print ("----------------------------------------------------------------")
            
            op = int(input('Digite una opcion: '))
            
            if op == 1:
                datos=self.SolicitarDatosCompletos()
                print(('no agregado', 'agregado con exito')[self.__miListaDeContactos.agregarContacto(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])])
                
            elif op == 2:
                contactos = self.__miListaDeContactos.darTodosLosContactos()
                print('contactos: ', contactos if contactos else 'no hay contactos registrados')
                
            elif op == 3:
                print(self.__miListaDeContactos.buscarContactosPalabraClave(input('Digite palabra clave: ')))
            elif op == 4:
                contacto=self.__miListaDeContactos.buscarContacto(input('Digite nombre: '), input('Digite apellido: '))
            elif op == 5:
                contacto=self.__miListaDeContactos.eliminarContacto(input("Digite nombre: "), input("Digite apellido: "))
            elif op == 6:
               print('Modificar Contacto')
               nombre = input("Digita el nombre del contacto a modificar: ")
               apellido = input("Digita el apellido del contacto a modificar: ")
               contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
               if not contacto:
                   print("El Contacto no existe")
               else:
                   print(f"Contacto encontrado: {contacto.darNombre()} {contacto.darApellido()}")
                   
                   print("")
                   nuevaDireccion = input("Digita la nueva direccion del contacto: ") or None
                   nuevoCorreo = input("") or None
                   nuevoTelefono = menu.AgregarTelefonos if input("Deseas modificar el telefono del contacto? (s/n): ") == "s" else None
                   nuevasPalabras = menu.AgregarPalabras if input("Deseas agregar palabras clave al contacto? (s/n): ") == "s" else None
                   
                   datosModificados = menu.obtenerListaDeContactos.modificarContacto(nombre, apellido, nuevaDireccion, nuevoCorreo, nuevoTelefono, nuevasPalabras)
                   if datosModificados:
                       print("Contacto modificado con exito")
                   else:
                       print("No se pudo modifcar el contacto")
                       
            print("Datos:", contacto.darNombre(), contacto.darApellido())
            print("Direccion:", contacto.darDireccion())
            print("correo electronico", contacto.darCorreo())
            print("Numeros telefonicos:")
            print(contacto.darTelefonos())
            print("Palabras claves:")
            print(contacto.darPalabras())
            
            elif op == 0:
                salir = True

        return "Adios"
    
    def MenuContacto(self):
        salir = False

        while not salir:
            
            print ("1. Actualizar palabras")
            print ("2. Actualizar telefonos")
            print ("0. Salir")
            
            op = int(input('Digite una opcion: '))
            
            if op == 1:
                print ("op 1")
            elif op == 0:
                salir = True
    
    def SolicitarDatosCompletos(self):
        nombre=input('Digite nombre: ')
        apellido=input('Digite apellido: ')
        direccion=input('Digite direccion: ')
        correo=input('Digite correo: ')
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