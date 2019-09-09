from .terrestrial import ITerrestrial 


class IRocky(ITerrestrial):

    def __init__(self):
        super().__init__()
        self.rocky = True