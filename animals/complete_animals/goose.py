from animals import Animal
from interfaces.type import IFlat
from interfaces import Identifiable


class Goose(Animal, IFlat, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose", 7)
        IFlat.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Trees", "Weeds", "Berries"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'The Nene Goeese ate {prey} for a meal')

    def __str__(self):
        return f'Nene Goose {self.id}. Watch me whip, whip'