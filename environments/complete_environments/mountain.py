from interfaces import Identifiable
from environments.complete_environments import Environment


class Mountain(Environment, Identifiable):

    def __init__(self):
        Environment.__init__(self, "mountain")
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.terrestrial and animal.rocky:
                self.contains_animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or animals that require vegetation")

    def add_plant(self, plant):
        try:
            if plant.rocky:
                self.contains_plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants flat land or flowing water.")
