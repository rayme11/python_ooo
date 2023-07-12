class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price


b1 = Book("Star Wars", "JD", 3.66)
b2 = Book("Star Wars II", "JD", 4.66)

print(b1)
print(b2)