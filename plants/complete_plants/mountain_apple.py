from plants import Plant
from interfaces.type import IRocky

class MountainApple(Plant, IRocky):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17, "high")
        IRocky.__init__(self)