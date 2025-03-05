from iAnimal import iAnimal
from animal import Animal
from animal_exotico import Animal_exotico
from boa_constrictor import Boa_constrictor
from huron import Huron


boa1 = Boa_constrictor("Boa bebe",10.5,2,"Brasil",5000)
boa2 = Boa_constrictor("Boa adulta",180.5,2,"Colombia",5000)
boa3 = Boa_constrictor("Boa joven",90.5,2,"Ecuador",5000)

boas = [boa1, boa2, boa3]

for boa in boas:
    print("Nombre: "+boa.obtener_nombre()+" Peso: "+str(boa.obtener_peso())+" Origen: "+boa.obtener_pais_origen()+" ratones comidos: "+str(boa.obtener_ratones_comidos()))

print(" ")
print("Boa: "+boa1.obtener_nombre())
print(" Sonido de la boa: "+boa1.hacer_sonido())
print(" Impuesto "+str(boa1.obtener_impuesto()))
print(" Valor del flete: "+str(boa1.calcular_flete()))
print(" Comiendo ...")
boa1.sumar_ratones_comidos()
print("Boa: nombre "+boa1.obtener_nombre()+" Peso: "+str(boa1.obtener_peso())+" Origen: "+boa1.obtener_pais_origen()+" ratones comidos: "+str(boa1.obtener_ratones_comidos()))
print(" Comiendo ...")
boa1.sumar_ratones_comidos()
print("Comiendo ...")
boa1.sumar_ratones_comidos()
print("Boa: nombre "+boa1.obtener_nombre()+" Peso: "+str(boa1.obtener_peso())+" Origen: "+boa1.obtener_pais_origen()+" ratones comidos: "+str(boa1.obtener_ratones_comidos()))

huron = Huron("Pepe",35.1,4,"Italia",2500)
print(" ")
print("Huron "+huron.obtener_nombre()+" Peso: "+str(huron.obtener_peso())+" Origen: "+huron.obtener_pais_origen())
print(" Sonido del Huron: "+huron.hacer_sonido())
print(" Impuesto "+str(huron.obtener_impuesto()))
print(" Valor del flete: "+str(huron.calcular_flete()))