from animals import Animal
from interfaces.type import IRocky
from interfaces.type import ICanopy
from interfaces import Identifiable


class Opeapea(Animal, IRocky, ICanopy, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Opeapea Bat", 2)
        IRocky.__init__(self)
        ICanopy.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Moths", "Beetles", "Termites", "Grass"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'The Opeapea ate the {prey} for a meal')

    def __str__(self):
        return f'Opeapea {self.id}. Sonar noise Sonar noise.'