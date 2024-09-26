from modulos.clases import *


atraccion_item_A = Atraccion("PaseoVerde",10,10,Estado.ACTIVO,0)
atraccion_item_B = Atraccion("PaseoAzul",5,10,Estado.ACTIVO,0)
atraccion_item_INF = Atraccion_Infantil(10,"PaseoInfantil",3,5,Estado.ACTIVO,0)
atraccion_item_MONTAÑA = Montaña_Rusa(10,100,1000,"MontañaRusa",20,10,Estado.ACTIVO,0)


visitante_item_a = Visitante("Benja",25,1.77,10000,0)
visitante_item_b = Visitante("Nico",20,1.80,5000,0)
visitante_item_c = Visitante("Benja",27,1.30,7000,0)



print (atraccion_item_INF.info())
print (atraccion_item_MONTAÑA.info())


