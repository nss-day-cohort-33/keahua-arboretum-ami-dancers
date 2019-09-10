from plants import Plant
from interfaces.type import ICanopy
from interfaces import Identifiable


class Rainbow(Plant, ICanopy, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Full", 8, "low")
        ICanopy.__init__(self)
        Identifiable.__init__(self)