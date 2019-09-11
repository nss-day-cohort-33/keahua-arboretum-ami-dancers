
from environments import Environments
from interfaces import Identifiable
# from interfaces.habitats import IStagnant


class Swamp(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "swamp")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        if len(self.contains_animals) < 9:
            try:
                if animal.stagnate:
                    self.contains_animals.append(animal)
            except AttributeError:
                print("Cannot add animals that need flowing water to the swamp.")
        else:
            print("This biome contains too many animals.")

    def add_plant(self, plant):
        if len(self.contains_plants) < 13:
            try:
                if plant.stagnate:
                    self.contains_plants.append(plant)
            except AttributeError:
                print("Cannot add plants that require flowing water")
        else:
            print("This biome contains too many plants.")

