
from environments import Environments
from interfaces import Identifiable
# from interfaces.habitats import IStagnant


class Swamp(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "swamp")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.stagnate:
                self.contains_animals.append(animal)
        except AttributeError:
            print("Cannot add animals that need flowing water to the swamp.")

    def add_plant(self, plant):
        try:
            if plant.stagnate:
                self.contains_plants.append(plant)
        except AttributeError:
            print("Cannot add plants that require flowing water")
