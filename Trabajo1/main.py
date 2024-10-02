from modulos.clases import *


atraccion_item_A = Atraccion(nombre="PaseoVerde",capacidad=10,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_B = Atraccion(nombre="PaseoAzul",capacidad=5,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_INF = Atraccion_Infantil(edad_limite=10,nombre="PaseoInfantil",capacidad=3,duracion=5,estado=Estado.ACTIVO,cola=0)
atraccion_item_MONTAÑA = Montaña_Rusa(velocidad_maxima=10,altura_maxima=140,extension=1000,nombre="MontañaRusa",capacidad=20,duracion=10,estado=Estado.ACTIVO,cola=0)


visitante_item_a = Visitante(nombre="Benja",edad=25,altura=1.77,dinero=10000,tickets=0)
visitante_item_b = Visitante(nombre="Nico",edad=20,altura=1.80,dinero=7000,tickets=0)
visitante_item_c = Visitante(nombre="Felipe",edad=7,altura=1.30,dinero=3000,tickets=0)


atraccion_item_INF.verificar_atraccion(visitante_item_a.edad)

print (visitante_item_a.info())
atraccion_item_A.comenzar_mantenimiento()
print (atraccion_item_A.estadoInfo())
atraccion_item_A.finalizar_mantenimiento()
print (atraccion_item_A.estadoInfo())

