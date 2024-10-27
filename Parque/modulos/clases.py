from enum import Enum
import random

class Estado(Enum):
      ACTIVO = 1
      FUERA_DE_SERVICIO = 0

class Visitante :

    visitantes = 0

    def __init__(self,nombre,edad,altura,dinero,tickets):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets
        Visitante.visitantes += 1
    
    # def info(self):
    #    return f"{self.nombre} - {self.edad} - {self.altura} - {self.dinero} - {self.tickets}"
    # Metodo para devolver la informacion de los objetos creados, utilizada para verificacion
    
    def contar_visitante(): # Metodo que retorna la cantidad de objetos creados, en este caso cuantos visitantes ingresan
        return Visitante.visitantes
        
    def comprar_ticket(self):
          
          pass
    
    def entregrar_ticket(self):
          pass
    
    def hacer_cola(self):
          pass
    def mostrar_dinero(self):
        print(f"A {self.nombre} le quedan {self.dinero}")
    
    
class Atraccion:
    def __init__(self,nombre,capacidad,duracion,estado,cola):
            self.nombre = nombre
            self.capacidad = capacidad
            self.duracion = duracion
            self.estado = estado
            self.cola = cola

    def info(self):
        return f"[Nombre: {self.nombre}]-[Capacidad: {self.capacidad}]-[Duracion: {self.duracion}]-[Estado: {self.estado}]-[Cola: {self.cola}]"

    def iniciar_ronda(self):
         print("Ronda Iniciada")

    def comenzar_mantenimiento(self):
        self.estado = Estado.FUERA_DE_SERVICIO
        
    def finalizar_mantenimiento(self):
        self.estado = Estado.ACTIVO
        
    def estadoInfo(self,numRandom):
        if numRandom == 1:
            Atraccion.comenzar_mantenimiento(self)
        else:
            Atraccion.finalizar_mantenimiento(self)
        
    
    

class Atraccion_Infantil(Atraccion):
    def __init__(self,edad_limite,nombre,capacidad,duracion,estado,cola):
        super().__init__(nombre,capacidad,duracion,estado,cola)
        self.edad_limite = edad_limite 
    
    def verificar_atraccion(self,edad_revision):#validar edad solo pueden 10 años o menos
        if(edad_revision > self.edad_limite):
            print("\nLa entrada a esta atraccion esta prohibida a mayores de 10 años, acceso denegado\n")

      
class Montaña_Rusa(Atraccion):
    def __init__(self,velocidad_maxima,altura_maxima,extension,nombre,capacidad,duracion,estado,cola):
      super().__init__(nombre,capacidad,duracion,estado,cola)
      self.velocidad_maxima = velocidad_maxima
      self.altura_maxima = altura_maxima
      self.extension = extension

    def verificar_atraccion(self):#validar altura solo pueden 140cm o mas
      pass
      
    def info(self):
      return f"{self.altura_maxima} - {self.nombre} - {self.duracion}"


class Ticket:
    def __init__(self,numero,atraccion,precio,fecha_compra):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra


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

    def resumen_de_ventas(self,dia):

        print(f"Dinero generado desde Apertura : {self.dinero_generado}")






