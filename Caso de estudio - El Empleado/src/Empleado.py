__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from Fecha import fecha

class Empleado:
    # Aqui inicia la decladracion de la clase 

    """#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#"""

    nombre = ""
    apellido = ""
    salario = 0

    """#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 1 = Masculino, y 2 = Femenino
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#"""

    sexo = 0

    """#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Asociacion 
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#"""

    fechaingreso = fecha()
    fechanacimiento = fecha()

    """#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#"""
    
    # Este metodo retorna el nombre del empleado
    def DarNombre(self): 
        # Aqui va mi codigo
        return self.nombre
    
    __method__ = "CambiarSalario"
    __paramter__ = "nuevosalrio"
    __returns__ = "salario"
    __Description__ = " metodo que actualzia el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        self.salario = nuevoSalario

    # Retorna le salrio del empleado
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario

    # Este metodo retorna la edad del empleado
    def CalcularEdad(self): ""
        # Aqui va mi codigo

    # Este metodo retorna la antiguedad del empleado en la empresa     
    def CalcularAntigueada(self): ""
         # Aqui va mi codigo
    
    __method__ = "CalcularSalarioAnual"
    __paramter__ = ""
    __returns__ = "salario anual"
    __Description__ = "Muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        #metodo 1
        #total = self.salario*12
        #metodo 2
        return self.salario*12
    
    __method__ = "CalcularImpuestoSalarioAnual"
    __paramter__ = ""
    __returns__ = "impuesto salario anual"
    __Description__ = "Muestra el impuesto del salario anual del empleado"
    def CalcularaImpuestoSalarioAnual(self):
        #_____Forma 1______
        #SalarioAnual = self.CalcularSalarioAnual()
        #impuestoAnual=SalarioAnual*19
        #return impuestoAnual
        #_____Forma 2______
        return self.CalcularSalarioAnual()*0.19 
    
    __method__ = "CalcularImpuestoSalarioMensual"
    __paramter__ = ""
    __returns__ = "impuesto salario mensual"
    __Description__ = "Muestra el impuesto del salario mensual del empleado"
    def CalcularSalarioMensula(self):
        return self.DarSalario()*0.19