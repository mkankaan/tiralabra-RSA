class Key:
    def __init__(self, n, e=None):
        self.modulus = n
        self.exponent = e

    # temporary format
    def __repr__(self):
     return "-".join((str(self.modulus), str(self.exponent)))
