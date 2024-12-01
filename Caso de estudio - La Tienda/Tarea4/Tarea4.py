__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

IVA_PAPELERIA = 0.16
IVA_SUPERMERCADO = 0.04
IVA_FARMACIA = 0.12

#--------------------------------
# Clase Producto
#--------------------------------
class Producto:
    #---------------------------------
    # Metodo Constructor
    #-------------------------------
    def __init__(self, nombre, tipo, valorUnitario, cantidadBodega, cantidadMinima, cantidadUnidadesVendidas):
        self.nombre = nombre
        self.tipo = tipo
        self.valorUnitario = valorUnitario
        self.cantidadBodega = cantidadBodega
        self.cantidadMinima = cantidadMinima
        self.cantidadUnidadesVendidas = cantidadUnidadesVendidas
        self.iva = self.definirIVA()
    #-----------------------------------
    # Metodos - Clase Producto
    #-----------------------------------
    
    def definirIVA(self):
        if self.tipo == "Papelería":
            return IVA_PAPELERIA
        elif self.tipo == "Supermercado":
            return IVA_SUPERMERCADO
        elif self.tipo == "Droguería":
            return IVA_FARMACIA
        else:
            return 0  

    def darNombre(self):
        return self.nombre

    def darTipo(self):
        return self.tipo

    def darValorUnitario(self):
        return self.valorUnitario

    def darIVA(self):
        return self.iva

    def darCantidadBodega(self):
        return self.cantidadBodega

    def darCantidadMinima(self):
        return self.cantidadMinima

    def darCantidadUnidadesVendidas(self):
        return self.cantidadUnidadesVendidas

    def vender(self, pCantidad):
        self.cantidadUnidadesVendidas += pCantidad
        self.cantidadBodega -= pCantidad

    def abastecer(self, pCantidad):
        self.cantidadBodega += pCantidad
        
    # Se vendieron 5 unidades del producto (suponga que hay suficientes).
    def venderCantidad(self, cantidad):
        self.cantidadUnidadesVendidas += cantidad
        self.darCantidadBodega -= cantidad
    
    # El valor unitario se incrementa en un 10% 
    def incrementarValor(self):
        self.valorUnitario *= 1.10
        
    # Se incrementa en uno la cantidad mínima para hacer pedidos.
    def incrementarCantidadMinima(self): 
        self.cantidadMinima += 1
        
    # El producto ahora se clasifica como de SUPERMERCADO
    def cambiarTipo(self):
        self.tipo = "SUPERMERCADO"
    
    # Se cambia el nombre del producto. Ahora se llama "teléfono".
    def cambiarNombre(self):
        self.nombre = "teléfono"

#-----------------------------------------------------------------------
# Clase Tienda
#------------------------------------------------------------------------
class Tienda:
    #-------------------------------------------------------------------------
    # Metodo Constructor
    #-------------------------------------------------------------------------
    def __init__(self, producto1, producto2, producto3, producto4, dineroEnCaja):
        self.producto1 = producto1
        self.producto2 = producto2
        self.producto3 = producto3
        self.producto4 = producto4
        self.dineroEnCaja = dineroEnCaja

    #-------------------------------------------------------------
    # Metodos - Clase Tienda
    #-----------------------------------------------------------
    

    def darProducto1(self):
        return self.producto1
    
    def darProducto2(self):
        return self.producto2

    def darProducto3(self):
        return self.producto3

    def darProducto4(self):
        return self.producto4

    def darDineroEnCaja(self):
        return self.dineroEnCaja

    # Se asigna al dinero en caja de la tienda la suma de los valores unitarios de los cuatro productos
    def asignarDineroEnCaja(self):
        self.dineroEnCaja = self.producto1.darValorUnitario() + \
                            self.producto2.darValorUnitario() + \
                            self.producto3.darValorUnitario() + \
                            self.producto4.darValorUnitario()

    # Se venden 4 unidades del producto 3 (suponga que estan disponibles)
    def venderProducto3(self):
        valorConIVA = self.producto3.darValorUnitario() * (1 + self.producto3.darIVA())
        self.producto3.vender(4)
        self.dineroEnCaja += valorConIVA * 4

    # Se disminuye en un 2%(*0.98) el dinero en la caja
    def disminuirDineroEnCaja(self):
        self.dineroEnCaja *= 0.98

    # Se abastece la tienda con la mitad de la cantidad minima de cada producto, suponiendo que la cantidad en bodega de todos los productos es menor a la cantidad minima
    def abastecerTienda(self):
        cantidadAbastecer1 = self.producto1.darCantidadMinima() // 2
        self.producto1.abastecer(cantidadAbastecer1)

        cantidadAbastecer2 = self.producto2.darCantidadMinima() // 2
        self.producto2.abastecer(cantidadAbastecer2)

        cantidadAbastecer3 = self.producto3.darCantidadMinima() // 2
        self.producto3.abastecer(cantidadAbastecer3)

        cantidadAbastecer4 = self.producto4.darCantidadMinima() // 2
        self.producto4.abastecer(cantidadAbastecer4)

    # Se pone en la caja el dinero correspondiente a las unidades vendidas de todos los productos de la tienda 
    def actualizarDineroPorVentas(self):
        totalVentas = (self.producto1.darValorUnitario() * self.producto1.darCantidadUnidadesVendidas() * (1 + self.producto1.darIVA())) + \
                      (self.producto2.darValorUnitario() * self.producto2.darCantidadUnidadesVendidas() * (1 + self.producto2.darIVA())) + \
                      (self.producto3.darValorUnitario() * self.producto3.darCantidadUnidadesVendidas() * (1 + self.producto3.darIVA())) + \
                      (self.producto4.darValorUnitario() * self.producto4.darCantidadUnidadesVendidas() * (1 + self.producto4.darIVA()))

        self.dineroEnCaja += totalVentas
