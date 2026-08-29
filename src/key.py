from typing import NamedTuple


class Key(NamedTuple):
    """A class to represent an RSA key.
    """

    modulus: int
    exponent: int

    def __repr__(self): # pragma: no cover
        return "-".join((str(self.modulus), str(self.exponent)))
