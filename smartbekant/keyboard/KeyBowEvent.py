class KeyBowEvent:
    index = None
    state = None

    def __init__(self, index: int, state: bool):
        self.index = index
        self.state = state
