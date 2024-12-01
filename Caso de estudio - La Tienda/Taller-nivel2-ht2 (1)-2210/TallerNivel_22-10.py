#----------------------------------------------------------------------------
# Nombre: Juan Camilo Parra Sanchez
# ID:  917079
#----------------------------------------------------------------------------
__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

#-----------------------------------------------------
# Clase Estudiante
#-----------------------------------------------------

class Estudiante():
    NOTA_PRUEBA_ACADEMICA = 3.25
    CANDIDATO_BECA = 4.75
    #-------------------------------------------------
    # Constructor
    #-------------------------------------------------
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo constructor de la clase"
    def  __init__(self, codigo, nombre, apellido):
    #-------------------------------------------------
    # Atributos
    #-------------------------------------------------
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.curso1 = Curso("", "", "", "")  
        self.curso2 = Curso("", "", "", "")  
        self.curso3 = Curso("", "", "", "")  
        self.curso4 = Curso("", "", "", "")  
    
    #-------------------------------------------------
    # Expresiones 
    #-------------------------------------------------   

    #-------------------------------------------------
    # Declaracion de Metodos
    #-------------------------------------------------
    
    #retorna el nombre del estudiante
    def darNombre(self):
        return self.nombre
    
    #indica si el el estudiante ya tiene los cuatro cursos pertenecen al mismo departamente 
    def pertenecenMismoDepartamento(self):
        mismoDepartamento = self.curso1.darDepartamento()
        if self.curso2.darDepartamento() !=  mismoDepartamento:
            return False
        if self.curso3.darDepartamento() !=  mismoDepartamento:
            return False
        if self.curso4.darDepartamento() !=  mismoDepartamento:
            return False
        else:
            return True

    
    #calcula el promedio de los cursos que ya tienen nota. si ningun curso tiene nota aisgana, retorna 0
    def calcularPromedioEstudiante(self):
        sumaTotal = 0.0  
        creditosTotales = 0.0  

        if self.curso1.estaCalificado():
            sumaTotal += self.curso1.darNota() * self.curso1.darCreditos()
            creditosTotales += self.curso1.darCreditos()

        if self.curso2.estaCalificado():
            sumaTotal += self.curso2.darNota() * self.curso2.darCreditos()
            creditosTotales += self.curso2.darCreditos()

        if self.curso3.estaCalificado():
            sumaTotal += self.curso3.darNota() * self.curso3.darCreditos()
            creditosTotales += self.curso3.darCreditos()

        if self.curso4.estaCalificado():
            sumaTotal += self.curso4.darNota() * self.curso4.darCreditos()
            creditosTotales += self.curso4.darCreditos()

        if creditosTotales == 0:
            return 0.0

        return sumaTotal / creditosTotales

    #Busca y retorna el curso que tiene el codigo que se recibe como parametro. si ningun curso tiene dicho codigo el motodo retorna null
    def buscarCurso(self, pCodigoCurso):
        if self.curso1.darCodigo() == pCodigoCurso:
            return self.curso1
        if  self.curso2.darCodigo() == pCodigoCurso:
            return self.curso2
        if  self.curso3.darCodigo() == pCodigoCurso:
            return self.curso3
        if  self.curso4.darCodigo() == pCodigoCurso:
            return self.curso4
        return None
    
    #Indica si el estudiante se encuentra en prueba academica. retorna verdadero si esta ne prueba academica, false de lo contrario
    def estaEnPrueba(self):
        return self.calcularPromedioEstudiante() < self.NOTA_PRUEBA_ACADEMICA

    
#-----------------------------------------------------
# Clase Curso
#-----------------------------------------------------

class Curso():
    MINIMA = 1.5
    MAXIMA  = 5.0
    #-------------------------------------------------
    # Constructor
    #-------------------------------------------------
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo constructor de la clase"
    def __init__(self, codigo, nombre, creditos, departamento, nota=0):
    #-------------------------------------------------
    # Atributos
    #-------------------------------------------------
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = 0
        self.departamento = departamento
        self.nota = nota
        
    #-------------------------------------------------
    # Declaracion de Metodos
    #-------------------------------------------------
    
    # Retorna el codigo del curso
    def darCodigo(self):
        return self.codigo
    
    #indica si el curso ya fue califica (tiene una nota distinta a 0)
    def estaCalificado(self):
        return self.nota != 0

    #-------------------------------------------------
    # Para el funcionamiento de el codigo
    #--------------------------------------------------
    def darNota(self):
        return self.nota
    def darDepartamento(self):
        return self.departamento
    def darCreditos(self):
        return self.creditos