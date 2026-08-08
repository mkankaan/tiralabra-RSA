from collections import namedtuple


class Key(namedtuple("Key", ["modulus", "exponent"])):
    def __repr__(self):
        return "-".join((str(self.modulus), str(self.exponent)))
