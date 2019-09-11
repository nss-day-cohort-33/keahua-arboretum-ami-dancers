from animals import Animal
from interfaces.type import ICanopy
from interfaces import Identifiable


class Gecko(Animal, ICanopy, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko", 2)
        ICanopy.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Cane Spider", "Cockroach", "Praying Mantid", "Walking Stick"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'\nThe Gecko ate the {prey} for a meal')

    def __str__(self):
        return f'\nGecko {self.id}. I can help you save a bunch of money on your car insurance by switching to Geico.'