from animals import Animal
from interfaces.type import IFreshwater
from interfaces.type import IStagnate
from interfaces import Identifiable


class Kikakapu(Animal, IFreshwater,IStagnate, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapu", 1)
        IFreshwater.__init__(self)
        IStagnate.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Trout", "Mackarel", "Salmon", "Sardine"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        print(f"The Kikakapu ate {prey} for a meal")

    def __str__(self):
        return f"Kikakapu {self.id}. Fish don't make noise, dummy."