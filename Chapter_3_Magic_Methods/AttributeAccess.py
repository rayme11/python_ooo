class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title} by author={self.author}, and the price is={self.price}"

    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)



b1 = Book("Star Wars", "JD", 3.66)
b2 = Book("Star Wars II", "JD", 4.66)

b1.price = 38.99
print(b1)