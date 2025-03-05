from models.animal_exotico import Animal_exotico

class Guarderia(Animal_exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        boa1 = Boa_constrictor("Boa bebe",10.5,2,"Brasil",5000)
        boa2 = Boa_constrictor("Boa adulta",180.5,2,"Colombia",5000)