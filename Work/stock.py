class Stock:
    __slots__ = ["name", "_shares", "price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, n):
        self.shares -= n

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, val):
        if not isinstance(val, int):
            raise TypeError("expected an integer")
        self._shares = val

    @property
    def cost(self):
        return self.shares * self.price
    
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.shares},{self.price})"