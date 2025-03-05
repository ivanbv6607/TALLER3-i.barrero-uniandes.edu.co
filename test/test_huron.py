import unittest

from models.huron import Huron
#from models.animal import Animal
#from models.animal_exotico import Animal_exotico
#from models.iAnimal import iAnimal


class Test_Huron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron= Huron(nombre="Flike", peso= 15.4, edad=3, pais_origen="Africa", impuestos=12)
        self.assertEqual(huron.hacer_sonido(),"!Eek Eek!")

    def test_calcular_flete(self):
        huron= Huron(nombre="Flike", peso= 15.4, edad=3, pais_origen="Africa", impuestos=12)
        self.assertEqual(huron.calcular_flete(),184.8)