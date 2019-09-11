
from interfaces import Identifiable
from environments import Environments


class Grassland(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "grassland")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        if len(self.contains_animals) < 23:
            try:
                if animal.terrestrial and animal.flat:
                    self.contains_animals.append(animal)
            except AttributeError:
                print("Cannot add aquatic, or animals that require high altitude.")
        else:
            print("This biome contains too many animals.")

    def add_plant(self, plant):
        if len(self.contains_plants) < 16:
            try:
                if plant.flat:
                    self.contains_plants.append(plant)
            except AttributeError:
                print("Cannot add plants that require high altitude.")
        else:
            print("This biome contains too many plants.")
