__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    __method__ = "Ahorrar"
    __parameter__ = ""
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite pasar el saldo de la cuenta corriente a la cuenta de ahorros"
    def Ahorrar(self ,Valor):
        Valor = self.__CuentaCorriente.DarSaldo()
        self.__CuentaCorriente.RetirarValor(Valor)
        self.__CuentaAhorros.ConsignarValor(Valor)
   
    __method__ = "DarSaldoCorriente"
    __paramter__ = "ninguno" 
    __returns__ = "Saldo de la Cuenta corriente"
    __Description__ = "Metodo que retorna el saldo de la cuenta corriente"
    def DarSaldoCorriente(self):
        return self.__CuentaCorriente.DarSaldo()
    
    __method__ = "RetirarTodo"
    __paramter__ = "ninguno" 
    __returns__ = "Ninguno"
    __Description__ = "Metodo que retira el valor seeccionada del saldo total"
    def RetirarTodo(self):
        self.__CuentaAhorros.RetirarValor(self.__CuentaAhorros.DarSaldo())
        self.__CuentaCorriente.RetirarValor(self.__CuentaCorriente.DarSaldo())

    __method__ = "MultiplicarAhorro"
    __paramter__ = "ninguno" 
    __returns__ = "Ninguno"
    __Description__ = "Metodo que duplica el Saldo en la cuenta de ahorros"
    def MultiplicaAhorros(self):
      self.__CuentaAhorros.ConsignarValor(self.__CuentaAhorros.DarSaldo())