from animals import Animal
from interfaces.type import IStagnate
from interfaces import Identifiable


class Spider(Animal, IStagnate, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy Face Spider", .5)
        IStagnate.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Moths", "Beetles", "Termites"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'The Spider ate the {prey} for a meal')

    def __str__(self):
        return f'Spider {self.id}. Salutations.'