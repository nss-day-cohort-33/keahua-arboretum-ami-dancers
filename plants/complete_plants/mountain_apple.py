from plants import Plant
from interfaces.type import IRocky
from interfaces import Identifiable


class MountainApple(Plant, IRocky, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17, "high")
        IRocky.__init__(self)
        Identifiable.__init__(self)