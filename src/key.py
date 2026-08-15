from collections import namedtuple


class Key(namedtuple("Key", ["modulus", "exponent"])):
    """A class to represent an RSA key.
    """

    def __repr__(self): # pragma: no cover
        return "-".join((str(self.modulus), str(self.exponent)))
