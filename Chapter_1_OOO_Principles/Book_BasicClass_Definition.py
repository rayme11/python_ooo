class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # Static method
    __booklist = None

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self, title='No title', booktype = 'HARDCOVER', author='No author', pages='No pages', price='No price'):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        # using class
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not valid book type")
        else:
            self.booktype = booktype



    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

    def getdiscount(self):
        return self._discount


b1 = Book('Winning mentality', price=200)
print(b1.title, ' and price is ', b1.price)


b2 = Book('Winning always', price=30.99)
print(b2.title, ' and price is ', b2.price)
# Applying book discount
b2.setdiscount(.25)
print(b2.title, ' and price is ', str(b2.getprice()) + ' with discount of ' + str(b2.getdiscount()))

# getting the type of object
print(type(b2))
print(isinstance(b1, Book))

# Getting class attributes
print('Book types: ', Book.getbooktypes())

# Using class attributes
b3 = Book('Winning always', price=30.67, booktype="HARDCOVER")

# Should throw error since booktype is not part of the attributes being defined
b4 = Book('Winnie the poh', price=30.67, booktype="EBOOK")

# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
thebooks.append(b3)
print(thebooks)
thebooks.append(b3)
print(thebooks)
