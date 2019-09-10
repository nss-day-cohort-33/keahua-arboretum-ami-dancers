from plants import Plant
from interfaces.type import IFlat
from interfaces.type import IStagnate
from interfaces import Identifiable


class BlueJade(Plant, IFlat, IStagnate, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0, "medium")
        IFlat.__init__(self)
        IStagnate.__init__(self)
        Identifiable.__init__(self)
