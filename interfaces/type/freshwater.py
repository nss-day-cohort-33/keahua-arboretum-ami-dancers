from .aquatic import IAquatic


class IFreshwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.hypertonic = True
