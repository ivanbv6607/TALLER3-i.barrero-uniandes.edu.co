import unittest

from models.boa_constrictor import Boa_constrictor
#from models.animal import Animal
#from models.animal_exotico import Animal_exotico
#from models.iAnimal import iAnimal


class Test_Boa_constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa_constrictor= Boa_constrictor(nombre="Lola", peso= 38.4, edad=3, pais_origen="Brasil", impuestos=19*2)
        self.assertEqual(boa_constrictor.hacer_sonido(),"!Tsss!")

    def test_calcular_flete(self):
        boa_constrictor= Boa_constrictor(nombre="Lola", peso= 38.4, edad=3, pais_origen="Brasil", impuestos=19*2)
        self.assertEqual(boa_constrictor.calcular_flete(),1459.2)

    def test_alimentar_boas(self):
        boa_constrictor= Boa_constrictor(nombre="Lola", peso= 38.4, edad=3, pais_origen="Brasil", impuestos=19*2)
        self.assertEqual(boa_constrictor.sumar_ratones_comidos(),None)

        