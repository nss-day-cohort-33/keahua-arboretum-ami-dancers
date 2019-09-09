import sys
sys.path.append('../')
from environments.complete_environments import Environment
# from interfaces.habitats import IStagnant



class Swamp(Environment):

    def __init__(self):
        Environment.__init__(self, "swamp")

    def add_animal(self, animal):
        try:
            if animal.stagnant:
                self.contains_animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add animals that need flowing water to the swamp.")

    def add_plant(self, plant):
        try:
            if plant.stagnant:
                self.contains_plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require flowing water")

