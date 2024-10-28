from enum import Enum
import random

class Estado(Enum):
      ACTIVO = 1
      FUERA_DE_SERVICIO = 0

class Visitante():
    #Contadores
    visitantes = 0
    #Contadores de cuantos tickets se tienen de cada juego en total dia tras dia
    ContVisA = 0
    ContVisB = 0
    ContVisC = 0
    ContVisD = 0

    def __init__(self,nombre,edad,altura,dinero,tickets):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets
        Visitante.visitantes += 1 #Contador para saber cuantos visitantes entran al parque
    
    # Metodo que retorna la cantidad de objetos creados, en este caso cuantos visitantes ingresan
    def contar_visitante(): 
        return Visitante.visitantes
        
    def comprar_ticket(self,atraccion):
        
        # 1 = Paseo Verde ; 2 = Paseo Azul ; 3 = Paseo Infantil ; 4 = Montaña Rusa
        if atraccion == 1:
            self.tickets[0] += 1
            Visitante.ContVisA +=1
        elif atraccion == 2:
            self.tickets[1] += 1
            Visitante.ContVisB +=1
        elif atraccion == 3:
            self.tickets[2] += 1
            Visitante.ContVisC +=1
        elif atraccion == 4:
            self.tickets[3] += 1
            Visitante.ContVisD +=1
    
    def entregrar_ticket(self,atraccion_eleccion,atraccion_nombre):
        
        #atraccion = a cual se va a subir
        if self.tickets[atraccion_eleccion-1] >= 1:
            self.tickets[atraccion_eleccion-1] -= 1
            print(f"{self.nombre} a entregado un ticket para {atraccion_nombre}")
        else:
            print("No tiene tickets para esa atraccion")
    
    def hacer_cola(self,atraccion):
        print(f"{self.nombre} esta haciendo cola en ",atraccion)

    def mostrar_dinero(self):
        print(f"A {self.nombre} le quedan {self.dinero}")
    
    
class Atraccion:

    def __init__(self,nombre,capacidad,duracion,estado,cola):
            self.nombre = nombre
            self.capacidad = capacidad
            self.duracion = duracion
            self.estado = estado
            self.cola = cola

    def iniciar_ronda(self,nombre,cola):
        
        if(nombre == "PaseoVerde" and cola > 0):
            self.cola -= 1
        elif(nombre == "PaseoAzul" and cola > 0):
            if(cola < 3):
                self.cola = 0
            else:
                self.cola -= 3
        elif(nombre == "PaseoInfantil" and cola > 0):
            if(cola < 2):
                self.cola = 0
            else:
                self.cola -= 2
        elif(nombre == "MontañaRusa" and cola > 0):
            self.cola -=1

        print(f"Se inicia la ronda de {nombre}, las personas que hay actualmente en cola son : {self.cola}")
    
    def contar_cola(self):
        self.cola += 1

    def estado_cola(self):
        print("La cola en ",self.nombre,"es de : ",self.cola)

    def comenzar_mantenimiento(self):
        self.estado = Estado.FUERA_DE_SERVICIO
        
    def finalizar_mantenimiento(self):
        self.estado = Estado.ACTIVO
        
    def estadoInfo(self,numRandom):# entra un numero random entre 1 a 10, si es igual o menor a 2 el juego entra en mantenimiento, sino sigue activo
        if numRandom <= 2:
            Atraccion.comenzar_mantenimiento(self)
        else:
            Atraccion.finalizar_mantenimiento(self)
            
    

class Atraccion_Infantil(Atraccion):
    def __init__(self,edad_limite,nombre,capacidad,duracion,estado,cola):
        super().__init__(nombre,capacidad,duracion,estado,cola)
        self.edad_limite = edad_limite 
    
    def verificar_atraccion(self,edad):#validar edad solo pueden 10 años o menos
        if(edad > self.edad_limite):
            print("\nLa entrada a esta atraccion esta prohibida a mayores de 10 años, acceso denegado\n")
            return False
        else:
            return True
      
class Montaña_Rusa(Atraccion):
    def __init__(self,velocidad_maxima,altura_maxima,extension,nombre,capacidad,duracion,estado,cola):
      super().__init__(nombre,capacidad,duracion,estado,cola)
      self.velocidad_maxima = velocidad_maxima
      self.altura_maxima = altura_maxima
      self.extension = extension

    def verificar_atraccion(self,altura):#validar altura solo pueden 140cm o mas
        if(altura < 140):
            print("\n No puede subir a la atraccion ya que esta chiquito")
            return False
        else:
            return True


class Ticket:
    #Contador de cuantos tickets en total se han vendido (creado)
    idTicket = 0
    def __init__(self,numero,atraccion,precio,fecha_compra):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra
        Ticket.idTicket += 1

    def getID(self):
        return Ticket.idTicket


class Parque():


    def __init__(self,nombre,juegos,dinero_generado):
        self.nombre = nombre
        self.juegos = juegos
        self.dinero_generado = dinero_generado

    def consultar_juegos_activos(self,estadoA,estadoB,estadoC,estadoD,nameA,nameB,nameC,nameD):
        # activo = 1
        # fuera_servicio = 0
        if estadoA == Estado.ACTIVO :
            print(f"{nameA} - en funcionamiento")
        elif estadoA == Estado.FUERA_DE_SERVICIO :
            print(f"{nameA} - en mantenimiento")
        if estadoB == Estado.ACTIVO :
            print(f"{nameB} - en funcionamiento")
        elif estadoB == Estado.FUERA_DE_SERVICIO :
            print(f"{nameB} - en mantenimiento")
        if estadoC == Estado.ACTIVO :
            print(f"{nameC} - en funcionamiento")
        elif estadoC == Estado.FUERA_DE_SERVICIO :
            print(f"{nameC} - en mantenimiento")
        if estadoD == Estado.ACTIVO :
            print(f"{nameD} - en funcionamiento")
        elif estadoD == Estado.FUERA_DE_SERVICIO:
            print(f"{nameD} - en mantenimiento")


      
    def cobrar_ticket(self,atraccionPrecio,visitanteDinero):
      
        visitanteDinero -= atraccionPrecio
        self.dinero_generado += atraccionPrecio

        return visitanteDinero

    def resumen_de_ventas(self,dia,dineroDia,tickets):

        print(f"Dinero generado durante el dia #{dia}: {dineroDia}")
        print(f"Dinero generado desde Apertura : {self.dinero_generado}")
        print(f"Tickets totales vendidos : {tickets}")






