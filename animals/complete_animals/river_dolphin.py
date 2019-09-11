from animals import Animal
from interfaces.type import IFreshwater
from interfaces.type import ISaltwater
from interfaces import Identifiable


class RiverDolphin(Animal, IFreshwater, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin", 13)
        IFreshwater.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Trout", "Mackarel", "Salmon", "Sardine"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f'The dolphin ate the {prey} for a meal')

    def __str__(self):
        return f'Dolphin {self.id}. REEEEEeee EeeEEeeeeEE!'
