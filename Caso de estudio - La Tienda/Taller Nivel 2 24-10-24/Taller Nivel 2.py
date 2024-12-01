#---------------------------------------------------------------
# Clase Candidato
#----------------------------------------------------------------
class candidato:
    # Atributos
    def __init__(self, nombre, partidoPolitico, costoDeCampania):
        self.nombre = nombre
        self.partidoPolitico = partidoPolitico
        self.costoDeCampania = costoDeCampania
        self.votos = 0
        self.votosGeneroMasculino = 0
        self.votosGeneroFemenino = 0
        self.votosrango1 = 0
        self.votosrango2 = 0
        self.votosrango3 = 0
          
    # getters and setters 
    def darNombre(self):
        return self.nombre
    def darPartidoPolitico(self):
        return self.partidoPolitico
    def darcostoDeCampania(self):
        return self.costoDeCampania
    def darVotos(self):
        return self.votos
    
    # dartotalVotosGeneroFemenino
    def darvotosGeneroFemenino(self):
        return self.votosGeneroFemenino
    
    # darTotalVotosGeneroMasculino
    def darvotosGeneroMasculino(self):
        return self.votosGeneroMasculino
    
    # darVotosRango1
    def darVotosRango1(self):
        return self.votosrango1
    
    # darVotosRango2
    def darvotosRango2(self):
        return self.votosrango2
    
    # darVotosRango3
    def darvotosRango3(self):
        return self.votosrango3
    
    # resgitrarVotos
    def registrarvotos(self, genero, edad, medio):
        self.votos += 1
        
        if genero == 'masculino':
            self.votosGeneroMasculino += 1
        if genero == 'femenino':
            self.votosGeneroFemenino += 1
            
        if edad > 20:
            self.votosrango1 += 1
        elif 21 <= edad <= 50:
            self.votosrango2 += 1
        elif edad > 50:
            self.votosrango3 += 1
            
        if  medio == 'Tv':
            self.costoDeCampania += 1000
        if medio == 'RADIO':
            self.costoDeCampania += 500
        if medio  == 'internet':
            self.costoDeCampania += 100  
    
    # reiniciar
    def reiniciar(self):
        self.votos = 0
        self.votosGeneroFemenino = 0
        self.votosGeneroMasculino = 0
        self.votosrango1 = 0
        self.votosrango2 = 0
        self.votosrango3 = 0
        self.costoDeCampania = 0
        
#---------------------------------------------------------------
# Clase Urna 
#----------------------------------------------------------------    
class urna:
    
    # Atributos
    def __init__(self):
        self.candidato1 = None
        self.candidato2 = None
        self.candidato3 = None

    # Getters and setters
    def darCandidato1(self):
        return self.candidato1
    
    # buscarCandidato(numero)
    def buscarCandidato(self, numero):
        if numero == 1:
            return self.candidato1
        if numero == 2:
            return self.candidato2
        if numero == 3:
            return self.candidato3
    
    # calcularTotalVotos
    def calcularTotalVotos(self):
        totalVotos = 0
        if self.candidato1:
            totalVotos += self.candidato1.darVotos()
        if self.candidato2:
            totalVotos += self.candidato2.darVotos()
        if self.candidato3:
            totalVotos += self.candidato3.darVotos()
        return totalVotos
    
    # calcularTotalVotosGeneroFemenino
    def calcularTotalVotosGeneroFemenino(self):
        totalVotosFemenino = 0
        if self.candidato1:
            totalVotosFemenino +=  self.candidato1.darvotosGeneroFemenino()
        if self.candidato2:
            totalVotosFemenino += self.candidato2.darvotosGeneroFemenino()
        if self.candidato3:
            totalVotosFemenino += self.candidato3.darvotosGeneroFemenino()
        return  totalVotosFemenino

    # calcularTotalVotosGeneroMasculino
    def calcularTotalVotosGeneroMasculino(self):
        totalVotosMasculino = 0
        if self.candidato1:
            totalVotosMasculino +=  self.candidato1.darvotosGeneroMasculino()
        if self.candidato2:
            totalVotosMasculino += self.candidato2.darvotosGeneroMasculino()
        if self.candidato3:
            totalVotosMasculino += self.candidato3.darvotosGeneroMasculino()
        return  totalVotosMasculino
    
    # darTotalVotosRangoEdad
    def darTotalVotosRangoEdad(self, edad):
        totalVotosRango = 0
        if edad > 20:
            rango = 1
        elif 21 <= edad <= 50:
            rango = 2
        elif edad > 50:
            rango = 3
        
        if self.candidato1:
            totalVotosRango += self.candidato1.darTotalVotosRangoEdad(rango)
        if self.candidato2:
            totalVotosRango += self.candidato2.darTotalVotosRangoEdad(rango)
        if self.candidato3:
            totalVotosRango += self.candidato3.darTotalVotosRangoEdad(rango)
        return totalVotosRango

    
    # calcularCostoPromedioCampania
    def calcularCostoPromedioCampania(self):
        totalCosto = 0
        if self.candidato1:
            totalCosto += self.candidato1.darcostoDeCampania
        if self.candidato2: 
            totalCosto += self.candidato2.darcostoDeCampania
        if self.candidato3: 
            totalCosto += self.candidato3.darcostoDeCampania
        return totalCosto / 3
    
    # calcularPorcentajeVotosCandidato(numero)
    def calcularProcentajevotosCandidato(self, numero):
        totalVotos = self.calcularTotalVotos()
        candidato = self.buscarCandidato(numero)
        
        if candidato:
            cantidadVotos = candidato.darVotos()
            return (cantidadVotos / totalVotos) * 100
        return 0

    # registrarVoto
    def registrarVoto(self, numero, genero, edad, medio):
        candidato = self.buscarCandidato(numero)
        if candidato:
            candidato.registrarVoto(self, numero, edad, medio)
        else:
            'el candidato no exisite' 
    
    # reiniciar
    def reiniciar(self):
        if self.candidato1:
            self.candidato1.reiniciar()
        if self.candidato2:
            self.candidato2.reiniciar()
        if self.candidato3:
            self.candidato3.reiniciar()
            

#---------------------------------------------------------------
# Clase votosRangoEdad
#----------------------------------------------------------------

class VotosRangoEdad:
    
    # Atributos
    def __init__(self):
        self.votosRango1Masculino = 0  
        self.votosRango2Masculino = 0 
        self.votosRango3Masculino = 0  
        self.votosRango1Femenino = 0
        self.votosRango2Femenino = 0
        self.votosRango3Femenino = 0

    # Get and Set
    
    def darTotalVotosRango1(self, genero):
        if genero == 'masculino':
            return self.votosRango1Masculino
        elif genero == 'femenino':
            return self.votosRango1Femenino

    def darTotalVotosRango2(self, genero):
        if genero == 'masculino':
            return self.votosRango2Masculino
        elif genero == 'femenino':
            return self.votosRango2Femenino

    def darTotalVotosRango3(self, genero):
        if genero == 'masculino':
            return self.votosRango3Masculino
        elif genero == 'femenino':
            return self.votosRango3Femenino

    # Registrar Voto
    def registrarVoto(self, genero, edad):
        if genero == 'masculino':
            if edad <= 20:
                self.votosRango1Masculino += 1
            elif 21 <= edad <= 50:
                self.votosRango2Masculino += 1
            elif edad > 50:
                self.votosRango3Masculino += 1
        elif genero == 'femenino':
            if edad <= 20:
                self.votosRango1Femenino += 1
            elif 21 <= edad <= 50:
                self.votosRango2Femenino += 1
            elif edad > 50:
                self.votosRango3Femenino += 1
                
    # Reiniciar
    def reiniciar(self):
        self.votosRango1Masculino = 0
        self.votosRango2Masculino = 0
        self.votosRango3Masculino = 0
        self.votosRango1Femenino = 0
        self.votosRango2Femenino = 0
        self.votosRango3Femenino = 0
