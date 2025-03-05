from models.animal import Animal
""" Se importa la clase padre Animal"""

class Animal_exotico(Animal):
    """ La clase Animal_exotico que hereda de Animal(nombre:str, peso:float, edad:int)
        tiene como atributos propios a: (pais_origen:str, impuestos:float)
        Métodos implementados:

        def obtener_pais_origen(self):
            return self._pais_origen
    
        def obtener_impuesto(self):
            return self._impuestos

        def calcular_flete(self):
            return round(self._impuestos*self._peso,2)    

       
    """
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def hacer_sonido(self):
        pass

    def obtener_pais_origen(self):
        return self._pais_origen
    
    def obtener_impuesto(self):
        return self._impuestos

    def calcular_flete(self):
        return round(self._impuestos*self._peso,2)    
    