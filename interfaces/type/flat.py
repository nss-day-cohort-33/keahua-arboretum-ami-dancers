from .terrestrial import ITerrestrial 


class IFlat(ITerrestrial):

    def __init__(self):
        super().__init__()
        self.flat = True