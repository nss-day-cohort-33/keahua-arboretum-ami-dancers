from plants import Plant
from interfaces.type import IFlat
from interfaces.type import IStagnate

class BlueJade(Plant, IFlat, IStagnate):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0, "medium")
        IFlat.__init__(self)
        IStagnate.__init__(self)
