from animals import Animal
from interfaces.type import ISaltwater
from interfaces import Identifiable


class Ulae(Animal, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "'Ulae", 1)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Trout", "Mackarel", "Salmon", "Sardine"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f"The 'Ulae ate {prey} for a meal")

    def __str__(self):
        return f"'Ulae {self.id}. Fish don't make noise, dummy."