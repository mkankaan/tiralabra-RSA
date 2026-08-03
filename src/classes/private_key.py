from classes.key import Key


class PrivateKey(Key):
    def __init__(self, n, e=None):
        super().__init__(n, e)
