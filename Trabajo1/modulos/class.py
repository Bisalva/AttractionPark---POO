
class Visitante:
    def __init__(self,nombre,edad,altura,dinero,tickets):
            self.nombre: nombre
            self.edad: edad
            self.altura: altura
            self.dinero: dinero
            self.tickets: tickets



        
    def comprar_ticket(self,Atraccion):
          pass
    
    def entregrar_ticket(self,Atraccion):
          pass
    
    def hacer_cola(self,Atraccion):
          pass




class Atraccion:
    def __init__(self,nombre,capacidad,duracion,estado,cola):
            self.nombre: nombre
            self.capacidad: capacidad
            self.duracion: duracion
            self.estado: estado
            self.cola: cola

    def iniciar_ronda(self):
         pass

    def comenzar_mantenimiento(self):
         pass

    def finalizar_mantenimiento(self):
         pass
    

class Ticket:
    def __init__(self,numero,atraccion,precio,fecha_comopra):
            self.numero: numero
            self.atraccion: atraccion
            self.precio: precio
            self.fecha_compra: fecha_comopra


class Parque:
      def __init__(self,nombre,juegos) -> None:
            pass
      
      def consultar_juegos_activos(self):
            pass
      
      def cobrar_ticket(self,Visitante,Atraccion):
            pass




