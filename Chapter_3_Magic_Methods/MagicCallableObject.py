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

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("Star Wars", "JD", 3.66)
b2 = Book("Star Wars II", "JD", 4.66)
b1("Anan thumbelina", "Joey", 45.44) # calling it as a function in case attributes change frequently - easy to ready
print(b1)