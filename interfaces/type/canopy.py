from .terrestrial import ITerrestrial 


class ICanopy(ITerrestrial):

    def __init__(self):
        super().__init__()
        self.canopy = True