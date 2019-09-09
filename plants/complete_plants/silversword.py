from plants import Plant
from interfaces.type import IFlat

class Silversword(Plant):

    def __init__(self):
        Plant.__init__("Silversword", "Shade", 22, "high")
        IFlat.__init__(self)