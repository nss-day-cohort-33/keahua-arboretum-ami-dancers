
from interfaces import Identifiable
from environments import Environments


class Forest(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "forest")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        if len(self.contains_animals) < 20:
            try:
                if animal.terrestrial and animal.canopy:
                    self.contains_animals.append(animal)
            except AttributeError:
                print("Cannot add aquatic, or animals that require open areas.")
        else:
            print("This biome contains too many animals.")

    def add_plant(self, plant):
        if len(self.contains_plants) < 32:
            try:
                if plant.canopy:
                    self.contains_plants.append(plant)
            except AttributeError:
                print("Cannot add plants that require high sun.")
        else:
            print("This biome contains too many plants.")
