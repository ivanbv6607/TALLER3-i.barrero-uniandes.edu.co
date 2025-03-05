from models.animal_exotico import Animal_exotico

class Huron(Animal_exotico):
    """     
    Clase Huron que hereda de la clase Animal_exotico(self, nombre:str, peso:float, edad:int, pais_origen:str, 
                                                                impuestos:float):

    Metodos implementados:

    def hacer_sonido(self):
            return "!Eek Eek!"
    """

    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        
    def hacer_sonido(self):
            return "!Eek Eek!"

    