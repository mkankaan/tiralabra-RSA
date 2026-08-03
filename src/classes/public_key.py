from classes.key import Key

class PublicKey(Key):
    def __init__(self, n, e=65537):
        super().__init__(n, e)
