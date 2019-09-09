import sys
sys.path.append('../')
from interfaces import IAquatic
from interfaces import Identifiable
from environments import Environments
from animals import RiverDolphin


class River(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "river")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.contains_animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    # def add_plant(self, plant):
    #     try:
    #         if plant.freshwater and plant.requires_current:
    #             self.contains_plants.append(plant)
    #     except AttributeError:
    #         raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
