from animals import Animal
from interfaces.type import ICanopy
from interfaces.type import IFlat
from interfaces import Identifiable


class Pueo(Animal, ICanopy, IFlat, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo", 13)
        ICanopy.__init__(self)
        IFlat.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Moongoose", "Field Mouse", "Black Rat"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'The Pueo ate the {prey} for a meal')

    def __str__(self):
        return f'Pueo {self.id}. Whooooo Whooo.'