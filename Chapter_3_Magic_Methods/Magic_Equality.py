class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare bookd to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)


b1 = Book("Star Wars", "JD", 3.66)
b2 = Book("Star Wars II", "JD", 4.66)
b3 = Book("Star Wars", "JD", 3.66)

print(b1 == b3) # should be false if __eq__ is not overriden as Python can't compare objects as such
print(b2 == b3)
print(b1 == 42)