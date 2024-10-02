from enum import Enum

class Estado(Enum):
      ACTIVO = 1
      FUERA_DE_SERVICIO = 2

class Visitante():
    def __init__(self,nombre,edad,altura,dinero,tickets):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets
    
    def info(self):
        print("opa")
        return f"{self.nombre} - {self.edad} - {self.altura} - {self.dinero} - {self.tickets}"
        
    def comprar_ticket(self):
          
          pass
    
    def entregrar_ticket(self):
          pass
    
    def hacer_cola(self):
          pass
    def returnEdad(self):
        return self.edad
    
    





class Atraccion:
    def __init__(self,nombre,capacidad,duracion,estado,cola):
            self.nombre = nombre
            self.capacidad = capacidad
            self.duracion = duracion
            self.estado = estado
            self.cola = cola


    def iniciar_ronda(self):
         pass

    def comenzar_mantenimiento(self):
        self.estado = Estado.FUERA_DE_SERVICIO
        print("Comenzó el Mantenimiento")
        
    def finalizar_mantenimiento(self):
        self.estado = Estado.ACTIVO
        print("Finalizó el Mantenimiento")

    def estadoInfo(self):
        return f"{self.estado}"
    
    

class Atraccion_Infantil(Atraccion):#Herencia revisar
    def __init__(self,edad_limite,nombre,capacidad,duracion,estado,cola):
        super().__init__(nombre,capacidad,duracion,estado,cola)
        self.edad_limite = edad_limite 

    def info(self):
        return f"{self.edad_limite} - {self.nombre}"
    
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
    def __init__(self,numero,atraccion,precio,fecha_comopra):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_comopra


class Parque:
      def __init__(self,nombre,juegos) -> None:
        pass
      
      def consultar_juegos_activos(self):
        pass
      
      def cobrar_ticket(self,Visitante,Atraccion):
        pass




