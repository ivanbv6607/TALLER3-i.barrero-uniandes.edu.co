from abc import ABC,abstractmethod

class iAnimal(ABC):
    """ Interface 
    Nombre : iAnimal
    Metodo : hacer_sonido() 
    """
    @abstractmethod
    def hacer_sonido(self):
        pass
