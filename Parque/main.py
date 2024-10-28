from modulos.clases import *
import random

parque = Parque(nombre="Praderas",juegos=["Paseo Verde","Paseo Azul","Paseo Infantil","Montaña Rusa"],dinero_generado=0)

atraccion_item_A = Atraccion(nombre="PaseoVerde",capacidad=1,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_B = Atraccion(nombre="PaseoAzul",capacidad=3,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_INF = Atraccion_Infantil(edad_limite=10,nombre="PaseoInfantil",capacidad=2,duracion=5,estado=Estado.ACTIVO,cola=0)
atraccion_item_MONTAÑA = Montaña_Rusa(velocidad_maxima=10,altura_maxima=140,extension=1000,nombre="MontañaRusa",capacidad=1,duracion=10,estado=Estado.ACTIVO,cola=0)
#Los parametros tienen su nombre correspondiente para un mayor entendimiento al ser muchas variables ; ej : nombre = "paseoInfantil"

visitante_item_a = Visitante(nombre="Benja",edad=25,altura=177,dinero=50000,tickets = [0,0,0,0])
visitante_item_b = Visitante(nombre="Nico",edad=20,altura=180,dinero=70000,tickets = [0,0,0,0])
visitante_item_c = Visitante(nombre="Felipe",edad=7,altura=130,dinero=30000,tickets = [0,0,0,0])
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
    atraccion_item_A.estadoInfo(random.randint(1,10))
    atraccion_item_B.estadoInfo(random.randint(1,10))
    atraccion_item_INF.estadoInfo(random.randint(1,10))
    atraccion_item_MONTAÑA.estadoInfo(random.randint(1,10))
    
    
    # Metodo que entrega una lista con el estado de cada juego ( Cada dia cambia )
    #parque.consultar_juegos_activos(atraccion_item_A.estado,atraccion_item_B.estado,atraccion_item_INF.estado,atraccion_item_MONTAÑA.estado,atraccion_item_A.nombre,atraccion_item_B.nombre,atraccion_item_INF.nombre,atraccion_item_MONTAÑA.nombre)

    
    
    # 1 = Paseo Verde ; 2 = Paseo Azul ; 3 = Paseo Infantil ; 4 = Montaña Rusa
    selecA = random.randint(1,4)
    selecB = random.randint(1,4)
    selecC = random.randint(1,4)

    contA = 0
    contB = 0
    contC = 0
    contD = 0


    if visitante_item_a.dinero != 0:
        
        if selecA == 1 and visitante_item_a.dinero >= 4000:
            ticketA = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            if atraccion_item_A.estado == Estado.ACTIVO:
                visitante_item_a.comprar_ticket(selecA)
                contA += 1
                visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
                print(" ",visitante_item_a.nombre,"a comprado 1 ticket para : ",ticketA.atraccion, " , con un valor de ",ticketA.precio)
            else:
                print("Paseo Verde esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecA == 2 and visitante_item_a.dinero >= 3000:
            ticketA = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            if atraccion_item_B.estado == Estado.ACTIVO:
                visitante_item_a.comprar_ticket(selecA)
                contB += 1
                visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
                print(" ",visitante_item_a.nombre,"a comprado 1 ticket para : ",ticketA.atraccion, " , con un valor de ",ticketA.precio)
            else:
                print("Paseo Azul esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecA == 3 and visitante_item_a.dinero >= 2000:
            ticketA = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            if atraccion_item_INF.estado == Estado.ACTIVO:
                visitante_item_a.comprar_ticket(selecA)
                contC += 1
                visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
                print(" ",visitante_item_a.nombre,"a comprado 1 ticket para : ",ticketA.atraccion, " , con un valor de ",ticketA.precio)
            else:
                print("Paseo Infantil esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecA == 4 and visitante_item_a.dinero >= 5000:
            ticketA = Ticket(Ticket.getID,"Montaña Rusa",5000,dia)
            if atraccion_item_MONTAÑA.estado == Estado.ACTIVO:
                visitante_item_a.comprar_ticket(selecA)
                contD += 1
                visitante_item_a.dinero = parque.cobrar_ticket(ticketA.precio,visitante_item_a.dinero)
                print(" ",visitante_item_a.nombre,"a comprado 1 ticket para : ",ticketA.atraccion, " , con un valor de ",ticketA.precio)
            else:
                print("Montaña Rusa esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        else :
            print(f"- {visitante_item_a.nombre} no tiene suficiente dinero")

    
    if visitante_item_b.dinero != 0:
        
        if selecB == 1 and visitante_item_b.dinero >= 4000:
            ticketB = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            if atraccion_item_A.estado == Estado.ACTIVO:
                visitante_item_b.comprar_ticket(selecB)
                contA += 1
                visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
                print(" ",visitante_item_b.nombre,"a comprado 1 ticket para : ",ticketB.atraccion, " , con un valor de ",ticketB.precio)
            else:
                print("Paseo Verde esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecB == 2 and visitante_item_b.dinero >= 3000:
            ticketB = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            if atraccion_item_B.estado == Estado.ACTIVO:
                visitante_item_b.comprar_ticket(selecB)
                contB += 1
                visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
                print(" ",visitante_item_b.nombre,"a comprado 1 ticket para : ",ticketB.atraccion, " , con un valor de ",ticketB.precio)
            else:
                print("Paseo Azul esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecB == 3 and visitante_item_b.dinero >= 2000:
            ticketB = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            if atraccion_item_INF.estado == Estado.ACTIVO:
                visitante_item_b.comprar_ticket(selecB)
                contC += 1
                visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
                print(" ",visitante_item_b.nombre,"a comprado 1 ticket para : ",ticketB.atraccion, " , con un valor de ",ticketB.precio)
            else:
                print("Paseo Infantil esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecB == 4 and visitante_item_b.dinero >= 5000:
            ticketB = Ticket(Ticket.getID,"Montaña Rusa",5000,dia)
            if atraccion_item_MONTAÑA.estado == Estado.ACTIVO:
                visitante_item_b.comprar_ticket(selecB)
                contD += 1
                visitante_item_b.dinero = parque.cobrar_ticket(ticketB.precio,visitante_item_b.dinero)
                print(" ",visitante_item_b.nombre,"a comprado 1 ticket para : ",ticketB.atraccion, " , con un valor de ",ticketB.precio)
            else:
                print("Montaña Rusa esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        else :
            print(f"- {visitante_item_b.nombre} no tiene suficiente dinero")
    
    
    if visitante_item_c.dinero != 0:
        
        if selecC == 1 and visitante_item_c.dinero >= 4000:
            ticketC = Ticket(Ticket.getID,"Paseo Verde",4000,dia)
            if atraccion_item_A.estado == Estado.ACTIVO:
                visitante_item_c.comprar_ticket(selecC)
                contA += 1
                visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
                print(" ",visitante_item_c.nombre,"a comprado 1 ticket para : ",ticketC.atraccion, " , con un valor de ",ticketC.precio)
            else:
                print("Paseo Verde esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecC == 2 and visitante_item_c.dinero >= 3000:
            ticketC = Ticket(Ticket.getID,"Paseo Azul",3000,dia)
            if atraccion_item_B.estado == Estado.ACTIVO:
                visitante_item_c.comprar_ticket(selecC)
                contB += 1
                visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
                print(" ",visitante_item_c.nombre,"a comprado 1 ticket para : ",ticketC.atraccion, " , con un valor de ",ticketC.precio)
            else:
                print("Paseo Azul esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecC == 3 and visitante_item_c.dinero >= 2000:
            ticketC = Ticket(Ticket.getID,"Paseo Infantil",2000,dia)
            if atraccion_item_INF.estado == Estado.ACTIVO:
                visitante_item_c.comprar_ticket(selecC)
                contC += 1
                visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
                print(" ",visitante_item_c.nombre,"a comprado 1 ticket para : ",ticketC.atraccion, " , con un valor de ",ticketC.precio)
            else:
                print("Paseo Infantil esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        elif selecC == 4 and visitante_item_c.dinero >= 5000:
            ticketC = Ticket(Ticket.getID,"Montaña Rusa",5000,dia)
            if atraccion_item_MONTAÑA.estado == Estado.ACTIVO:
                visitante_item_c.comprar_ticket(selecC)
                contD += 1
                visitante_item_c.dinero = parque.cobrar_ticket(ticketC.precio,visitante_item_c.dinero)
                print(" ",visitante_item_c.nombre,"a comprado 1 ticket para : ",ticketC.atraccion, " , con un valor de ",ticketC.precio)
            else:
                print("Montaña Rusa esta en mantenimiento por lo que no pude ser usado hoy")
                Ticket.idTicket -= 1

        else :
            print(f"- {visitante_item_c.nombre} no tiene suficiente dinero")
    

    print("\n")


    visitante_item_a.entregrar_ticket(selecA,ticketA.atraccion)
    #AQUI RESTRICCION
    

    if(ticketA.atraccion == "Paseo Verde" and atraccion_item_A.estado == Estado.ACTIVO):
        visitante_item_a.hacer_cola(atraccion_item_A.nombre)
        atraccion_item_A.contar_cola()
    if(ticketA.atraccion == "Paseo Azul" and atraccion_item_B.estado == Estado.ACTIVO):
        visitante_item_a.hacer_cola(atraccion_item_B.nombre)
        atraccion_item_B.contar_cola()
    if(ticketA.atraccion == "Paseo Infantil" and atraccion_item_INF.estado == Estado.ACTIVO):
        if atraccion_item_INF.verificar_atraccion(visitante_item_a.edad) == True:
            visitante_item_a.hacer_cola(atraccion_item_INF.nombre)
            atraccion_item_INF.contar_cola()
    if(ticketA.atraccion == "Montaña Rusa" and atraccion_item_MONTAÑA.estado == Estado.ACTIVO):
        if atraccion_item_MONTAÑA.verificar_atraccion(visitante_item_a.altura) == True:
            visitante_item_a.hacer_cola(atraccion_item_MONTAÑA.nombre)
            atraccion_item_MONTAÑA.contar_cola()
        
    
    print("\n")
    visitante_item_b.entregrar_ticket(selecB,ticketB.atraccion)

    if(ticketB.atraccion == "Paseo Verde" and atraccion_item_A.estado == Estado.ACTIVO):
        visitante_item_b.hacer_cola(atraccion_item_A.nombre)
        atraccion_item_A.contar_cola()
    if(ticketB.atraccion == "Paseo Azul" and atraccion_item_B.estado == Estado.ACTIVO):
        visitante_item_b.hacer_cola(atraccion_item_B.nombre)
        atraccion_item_B.contar_cola()
    if(ticketB.atraccion == "Paseo Infantil" and atraccion_item_INF.estado == Estado.ACTIVO):
        if atraccion_item_INF.verificar_atraccion(visitante_item_b.edad) == True:
            visitante_item_b.hacer_cola(atraccion_item_INF.nombre)
            atraccion_item_INF.contar_cola()
    if(ticketB.atraccion == "Montaña Rusa" and atraccion_item_MONTAÑA.estado == Estado.ACTIVO):
        if atraccion_item_MONTAÑA.verificar_atraccion(visitante_item_b.altura) == True:
            visitante_item_b.hacer_cola(atraccion_item_MONTAÑA.nombre)
            atraccion_item_MONTAÑA.contar_cola()
    
    print("\n")
    visitante_item_c.entregrar_ticket(selecC,ticketC.atraccion)

    if(ticketC.atraccion == "Paseo Verde" and atraccion_item_A.estado == Estado.ACTIVO):
        visitante_item_c.hacer_cola(atraccion_item_A.nombre)
        atraccion_item_A.contar_cola()
    if(ticketC.atraccion == "Paseo Azul" and atraccion_item_B.estado == Estado.ACTIVO):
        visitante_item_c.hacer_cola(atraccion_item_B.nombre)
        atraccion_item_B.contar_cola()
    if(ticketC.atraccion == "Paseo Infantil" and atraccion_item_INF.estado == Estado.ACTIVO):
        if atraccion_item_INF.verificar_atraccion(visitante_item_c.edad) == True:
            visitante_item_c.hacer_cola(atraccion_item_INF.nombre)
            atraccion_item_INF.contar_cola()
    if(ticketC.atraccion == "Montaña Rusa" and atraccion_item_MONTAÑA.estado == Estado.ACTIVO):
        if atraccion_item_MONTAÑA.verificar_atraccion(visitante_item_c.altura) == True:
            visitante_item_c.hacer_cola(atraccion_item_MONTAÑA.nombre)
            atraccion_item_MONTAÑA.contar_cola()

    print("\n")

    atraccion_item_A.estado_cola()
    atraccion_item_B.estado_cola()
    atraccion_item_INF.estado_cola()
    atraccion_item_MONTAÑA.estado_cola()

    print("\n")

    while True:
        print("\n")
        if atraccion_item_A.cola != 0:
            atraccion_item_A.iniciar_ronda(atraccion_item_A.nombre,atraccion_item_A.cola)
        if atraccion_item_B.cola != 0:
            atraccion_item_B.iniciar_ronda(atraccion_item_B.nombre,atraccion_item_B.cola)
        if atraccion_item_INF.cola !=0:
            atraccion_item_INF.iniciar_ronda(atraccion_item_INF.nombre,atraccion_item_INF.cola)
        if atraccion_item_MONTAÑA.cola !=0:
            atraccion_item_MONTAÑA.iniciar_ronda(atraccion_item_MONTAÑA.nombre,atraccion_item_MONTAÑA.cola)

        if atraccion_item_A.cola != 0 or atraccion_item_B.cola != 0 or atraccion_item_INF.cola != 0 or atraccion_item_MONTAÑA.cola != 0:
            print("\n")
            if atraccion_item_A.cola != 0:
                atraccion_item_A.iniciar_ronda(atraccion_item_A.nombre,atraccion_item_A.cola)
            if atraccion_item_B.cola != 0:
                atraccion_item_B.iniciar_ronda(atraccion_item_B.nombre,atraccion_item_B.cola)
            if atraccion_item_INF.cola !=0:
                atraccion_item_INF.iniciar_ronda(atraccion_item_INF.nombre,atraccion_item_INF.cola)
            if atraccion_item_MONTAÑA.cola !=0:
                atraccion_item_MONTAÑA.iniciar_ronda(atraccion_item_MONTAÑA.nombre,atraccion_item_MONTAÑA.cola)

        
        if atraccion_item_A.cola == 0 and atraccion_item_B.cola == 0 and atraccion_item_INF.cola == 0 and atraccion_item_MONTAÑA.cola == 0:
            break        



    print("\n")

    visitante_item_a.mostrar_dinero()
    visitante_item_b.mostrar_dinero()
    visitante_item_c.mostrar_dinero()

    print("\n")


    dineroDiaCierre = visitante_item_a.dinero + visitante_item_b.dinero + visitante_item_c.dinero
    dineroDiaTotal = dineroDiaEntrada - dineroDiaCierre
    print(f"\nSe vendieron {contA} tickets de Paseo Verde , {contB} tickets de Paseo Azul, {contC} tickets de Paseo Infantil y {contD} de montaña rusa el dia de hoy")

    #Print de las ganancias desde la apertura
    parque.resumen_de_ventas(dia,dineroDiaTotal,Ticket.idTicket)
    print(f"\nSe han vendido desde la apertura {Visitante.ContVisA} tickets de Paseo Verde, {Visitante.ContVisB} de Paseo Azul, {Visitante.ContVisC} de Paseo Infantil y {Visitante.ContVisD} de Montaña Rusa")
    opcion = int(input("\nSalir de la Simulacion del Parque :\n 1 - SI \n 2 - NO \n Opcion : "))
    print("\n")
    #opcion = 1
    if opcion == 1 :
        break
    


