from plants import Plant
from interfaces.type import ICanopy

class Rainbow(Plant):

    def __init__(self, ICanopy):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Full", 8, "low")
        ICanopy.__init__(self)