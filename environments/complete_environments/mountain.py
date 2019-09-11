
from interfaces import Identifiable
from environments import Environments


class Mountain(Environments, Identifiable):

    def __init__(self):
        Environments.__init__(self, "mountain")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        if len(self.contains_animals) < 6:
            try:
                if animal.terrestrial and animal.rocky:
                    self.contains_animals.append(animal)
            except AttributeError:
                print("Cannot add aquatic, or animals that require vegetation")
        else:
            print("This biome contains too many animals.")

    def add_plant(self, plant):
        if len(self.contains_plants) < 4:
            try:
                if plant.rocky:
                    self.contains_plants.append(plant)
            except AttributeError:
                print("Cannot add plants flat land or flowing water.")
        else:
            print("This biome contains too many animals.")
