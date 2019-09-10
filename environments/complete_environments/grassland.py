
from interfaces import Identifiable
from environments import Environments


class Grassland(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "grassland")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.flat:
                self.contains_animals.append(animal)
        except AttributeError:
            print("Cannot add aquatic, or animals that require high altitude.")

    def add_plant(self, plant):
        try:
            if plant.flat:
                self.contains_plants.append(plant)
        except AttributeError:
            print("Cannot add plants that require high altitude.")
