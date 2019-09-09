from interfaces import Identifiable
from environments.complete_environments import Environment


class Forest(Environment, Identifiable):

    def __init__(self):
        Environment.__init__(self, "forest")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.canopy:
                self.contains_animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or animals that require open areas.")

    def add_plant(self, plant):
        try:
            if plant.canopy:
                self.contains_plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require high sun.")
