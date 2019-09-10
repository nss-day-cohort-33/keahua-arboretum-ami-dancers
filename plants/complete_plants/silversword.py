from plants import Plant
from interfaces.type import IFlat
from interfaces import Identifiable


class Silversword(Plant, IFlat, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Silversword", "Shade", 22, "high")
        IFlat.__init__(self)
        Identifiable.__init__(self)
