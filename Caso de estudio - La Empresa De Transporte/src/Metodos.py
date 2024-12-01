__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"


#-------------------------------------------------------------------
# Clase Camion 
#--------------------------------------------------------------------
class camion:

    def __init__(self, matricula,capacidad, consumo, cargaActual=0):
        self.matricula = matricula
        self.capacidad = capacidad
        self.consumo = consumo
        self.cargaActual = cargaActual
    # ----------------------------------------------------------------
    # Metodos
    # ----------------------------------------------------------------

    __method__ = "darCapacidad"
    __params__ = "Ninguno"
    __returns__ = "Capacidad maxima de carga de el camion en Kg"
    __descriptions__ = (
        "retorna la capacidad de carga maxima del camion especificado en    Kg"
    )

    def darCapacidad(self):
        return self.capacidad

    __method__ = "darConsumo"
    __params__ = "Ninguno"
    __returns__ = "El consumo de gasolina en galones por kilometro "
    __descriptions__ = (
        "retorna el consumo de gasolina del camion en galones por kilometro "
    )

    def darConsumo(self):
        return self.consumo

    __method__ = "darMatricula"
    __params__ = "Ninguno"
    __returns__ = "Matricula del camion"
    __descriptions__ = (
        "Retorna la matricula del camion seleccionado, el cual es su identificador"
    )

    def darMatricula(self):
        return self.Matricula

    __method__ = "darCargaActual"
    __params__ = "Ninguno"
    __returns__ = "Carga actual del camion"
    __descriptions__ = "Retorna la carga actual que el camion esta transportando en kg"

    def darCargaActual(self):
        return self.cargaActual

    __method__ = "Cargar"
    __params__ = "carga"
    __returns__ = "True Cuando se añade la carga, False si la carga excede la capacidad del camion"
    __descriptions__ = "Añade una carga especifica al camion, si esta no excede la capacidad maxima del mismo"

    #def Cargar(self, carga):
    #    self.cargaActual += (carga + self.cargaActual <= self.capacidad) * carga
    #    return self.cargaActual + carga <= self.capacidad
    def  Cargar(self, carga):
        if self.carga_actual  + carga <= self.capacidad:
            self.carga_actual += carga
            return True
        else:
            return False


    __method__ = "Descargar"
    __params__ = "carga"
    __returns__ = "True si la descarga fue exitosa, False si no hay suficiente carga que descargar "
    __descriptions__ = "descarga una cantidad especifica del camion"

    #def Descargar(self, carga):
    #    self.cargaActual -= (self.cargaActual >= carga) * carga
    #    return self.cargaActual >= carga
    def Descargar(self, carga):
        if self.carga_actual >= carga:
            self.carga_actual -= carga
            return True
        else:
            return False

#----------------------------------------------------------
# Clase EmpresaTransporte
#----------------------------------------------------------

