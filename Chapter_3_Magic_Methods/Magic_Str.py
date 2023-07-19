class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title} by author={self.author}, and the price is={self.price}"



b1 = Book("Star Wars", "JD", 3.66)
b2 = Book("Star Wars II", "JD", 4.66)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))