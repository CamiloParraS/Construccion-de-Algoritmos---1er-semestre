__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []

    def darTodosLosContactos(self):
        return [f"{contacto.darNombre()} {contacto.darApellido()}" for contacto in self.contactos] 
 
    def buscarContactosPalabraClave(self, palabra):
        resultado = []
        for contacto in self.contactos:
            nombre = contacto.darNombre()
            apellido = contacto.darApellido()
            palabras_clave = contacto.darPalabras()
        
            if palabra in palabras_clave:
                resultado.append(f"{nombre} {apellido}")
                
            elif palabra in nombre:
                resultado.append(f"{nombre} {apellido}")
                
            elif palabra in apellido:
                resultado.append(f"{nombre} {apellido}")
            return resultado
    
    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido):
            return 0
        nuevoContacto = Contacto(nombre, apellido, direccion, correo)
        for telefono in telefonos:
            nuevoContacto.agregarTelefono(telefono)
        for palabra in palabras:
            nuevoContacto.agregarPalabra(palabra)
        self.contactos.append(nuevoContacto)
        return 1

    def eliminarContacto(self, nombre, apellido):
        contactoaEliminar = self.buscarContacto(nombre, apellido)
        if contactoaEliminar:
            self.contactos.remove(contactoaEliminar)

    def modificarContacto(self, nombre, apellido=None, direccion=None, correo=None, telefonos=None, palabras=None):
        contactoAModificar = self.buscarContacto(nombre, apellido)
        if contactoAModificar:
            contactoAModificar.direccion = direccion
            contactoAModificar.correo = correo
            contactoAModificar.telefonos = telefonos
            contactoAModificar.palabras = palabras

    def actualizarTelefonos(self, telefonos, contacto):
        contacto.telefonos = telefonos  

    def actualizarPalabras(self, palabras, contacto):
        contacto.palabras = palabras  

    def metodo1(self):
        pass

    def metodo2(self):
        pass