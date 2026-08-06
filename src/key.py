class Key:
    def __init__(self, modulus, exponent):
        self.modulus = modulus
        self.exponent = exponent


    def __repr__(self):
     return "-".join((str(self.modulus), str(self.exponent)))
