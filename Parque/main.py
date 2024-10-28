from modulos.clases import *
import random

parque = Parque(nombre="Praderas",juegos=["Paseo Verde","Paseo Azul","Paseo Infantil","Montaña Rusa"],dinero_generado=0)

atraccion_item_A = Atraccion(nombre="PaseoVerde",capacidad=10,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_B = Atraccion(nombre="PaseoAzul",capacidad=5,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_INF = Atraccion_Infantil(edad_limite=10,nombre="PaseoInfantil",capacidad=3,duracion=5,estado=Estado.ACTIVO,cola=0)
atraccion_item_MONTAÑA = Montaña_Rusa(velocidad_maxima=10,altura_maxima=140,extension=1000,nombre="MontañaRusa",capacidad=20,duracion=10,estado=Estado.ACTIVO,cola=0)
#Los parametros tienen su nombre correspondiente para un mayor entendimiento al ser muchas variables ; ej : nombre = "paseoInfantil"

visitante_item_a = Visitante(nombre="Benja",edad=25,altura=1.77,dinero=5000,tickets = [0,0,0,0])
visitante_item_b = Visitante(nombre="Nico",edad=20,altura=1.80,dinero=7000,tickets = [0,0,0,0])
visitante_item_c = Visitante(nombre="Felipe",edad=7,altura=1.30,dinero=3000,tickets = [0,0,0,0])
#En mi script se usaran 3 objetos visitante, pero se pueden agregar los que se requieran

dia = 0
opcion = 0

while True :

    dia += 1
    dineroDiaEntrada = visitante_item_a.dinero + visitante_item_b.dinero + visitante_item_c.dinero
    dineroDiaTotal = 0

    print("\n====Parque de Atracciones====\n")
    print("Dia : ",dia)
    print(f"El dia de hoy entran al parque {Visitante.contar_visitante()} visitantes")


    # Configuracion del estado inicial del parque (CAMBIAR A METODO) - Necesario un archivo extra para los metodos y simplificar el script
    print("\nEstado del Parque : \n")
    atraccion_item_A.estadoInfo(random.randint(1,2))
    atraccion_item_B.estadoInfo(random.randint(1,2))
    atraccion_item_INF.estadoInfo(random.randint(1,2))
    atraccion_item_MONTAÑA.estadoInfo(random.randint(1,2))
    
    # Metodo que entrega una lista con el estado de cada juego ( Cada dia cambia )
    #parque.consultar_juegos_activos(atraccion_item_A.estado,atraccion_item_B.estado,atraccion_item_INF.estado,atraccion_item_MONTAÑA.estado,atraccion_item_A.nombre,atraccion_item_B.nombre,atraccion_item_INF.nombre,atraccion_item_MONTAÑA.nombre)

    
    
    # 1 = Paseo Verde ; 2 = Paseo Azul ; 3 = Paseo Infantil ; 4 = Montaña Rusa
    selecA = random.randint(1,4)
    selecB = random.randint(1,4)
    selecC = random.randint(1,4)

    if visitante_item_a.dinero >= 2000:
        
        if selecA == 1 and visitante_item_a.dinero >= 4000:
            ticketA = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            visitante_item_a.comprar_ticket(selecA)
            visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
            print("1")

        elif selecA == 2 and visitante_item_a.dinero >= 3000:
            ticketA = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            visitante_item_a.comprar_ticket(selecA)
            visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
            print("2")

        elif selecA == 3 and visitante_item_a.dinero >= 2000:
            ticketA = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            visitante_item_a.comprar_ticket(selecA)
            visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
            print("3")

        elif selecA == 4 and visitante_item_a.dinero >= 5000:
            ticketA = Ticket(Ticket.getID,"Paseo Verde",5000,dia)
            visitante_item_a.comprar_ticket(selecA)
            visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
            print("4")

        else :
            print(f"- {visitante_item_a.nombre} no tiene suficiente dinero")

    
    if visitante_item_b.dinero >= 2000:
        
        if selecB == 1 and visitante_item_b.dinero >= 4000:
            ticketB = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            visitante_item_b.comprar_ticket(selecB)
            visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
            print("1")

        elif selecB == 2 and visitante_item_b.dinero >= 3000:
            ticketB = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            visitante_item_b.comprar_ticket(selecB)
            visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
            print("2")

        elif selecB == 3 and visitante_item_b.dinero >= 2000:
            ticketB = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            visitante_item_b.comprar_ticket(selecB)
            visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
            print("3")

        elif selecB == 4 and visitante_item_b.dinero >= 5000:
            ticketB = Ticket(Ticket.getID,"Paseo Verde",5000,dia)
            visitante_item_b.comprar_ticket(selecB)
            visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
            print("4")

        else :
            print(f"- {visitante_item_b.nombre} no tiene suficiente dinero")
    
    
    if visitante_item_c.dinero >= 2000:
        
        if selecC == 1 and visitante_item_c.dinero >= 4000:
            ticketC = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            visitante_item_c.comprar_ticket(selecC)
            visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
            print("1")

        elif selecC == 2 and visitante_item_c.dinero >= 3000:
            ticketC = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            visitante_item_c.comprar_ticket(selecC)
            visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
            print("2")

        elif selecC == 3 and visitante_item_c.dinero >= 2000:
            ticketC = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            visitante_item_c.comprar_ticket(selecC)
            visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
            print("3")

        elif selecC == 4 and visitante_item_c.dinero >= 5000:
            ticketC = Ticket(Ticket.getID,"Paseo Verde",5000,dia)
            visitante_item_c.comprar_ticket(selecC)
            visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
            print("4")

        else :
            print(f"- {visitante_item_c.nombre} no tiene suficiente dinero")
    


    print("\n")
    visitante_item_a.mostrar_dinero()
    visitante_item_b.mostrar_dinero()
    visitante_item_c.mostrar_dinero()

    print("\n")


    dineroDiaCierre = visitante_item_a.dinero + visitante_item_b.dinero + visitante_item_c.dinero
    dineroDiaTotal = dineroDiaEntrada - dineroDiaCierre

    #Print de las ganancias desde la apertura
    parque.resumen_de_ventas(dia,dineroDiaTotal)

    opcion = int(input("\nSalir de la Simulacion del Parque :\n 1 - SI \n 2 - NO \n Opcion : "))
    print("\n")
    #opcion = 1
    if opcion == 1 :
        break
    






# visitante_item_a.dinero = parque.cobrar_ticket(1000,visitante_item_a.dinero) - ej : Actualizar valores de 1 objeto
# atraccion_item_INF.verificar_atraccion(visitante_item_a.edad) - Llama a una funcion con parametros a usar 
# atraccion_item_A.iniciar_ronda() - Llama la funcion
# atraccion_item_INF.iniciar_ronda() Llama la funcion desde la Herencia
# print (atraccion_item_INF.info()) - Imprime la informacion de Atraccion (Herencia)
# print (atraccion_item_A.estadoInfo()) - Imprime la informacion de Atraccion
# print (visitante_item_a.info()) - Imprime la informacion de Visitante

