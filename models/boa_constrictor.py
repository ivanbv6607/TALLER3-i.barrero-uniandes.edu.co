from models.animal_exotico import Animal_exotico
"""
    Clase Boa_constrictor que hereda de la clase Animal_exotico(self, nombre:str, peso:float, edad:int, pais_origen:str, 
                                                                impuestos:float):
    Tiene como atributo propio _ratones_comidos:int
    
    Metodos implementados:
    def hacer_sonido(self):
            return "!Tsss!"
    
       
    def sumar_ratones_comidos(self):
        self._ratones_comidos += 1
    
    def obtener_ratones_comidos(self):
        return self._ratones_comidos

"""
class Boa_constrictor(Animal_exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 11
    
    def hacer_sonido(self):
            return "!Tsss!"
    
    def sumar_ratones_comidos(self):
        if self._ratones_comidos > 20:
            raise ValueError ("Demasiados Ratones")
        self._ratones_comidos += 11
    
    def obtener_ratones_comidos(self):
        return self._ratones_comidos