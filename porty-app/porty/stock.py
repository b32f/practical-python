from .typedproperty import Float, Integer, String


class Stock:
    __slots__ = ["_name", "_shares", "_price"]

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, n):
        self.shares -= n

    @property
    def cost(self):
        return self.shares * self.price
    
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.shares},{self.price})"