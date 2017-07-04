import abc


class Textbook(object):
    """Define Textbook as an abstract base class"""
    __metaclass__ = abc.ABCMeta
    initial_sale_price = 0
    pages = 0

    def __init__(self, year, author, edition, sold_on):
        """class constructor method"""
        self.year = year
        self.author = author
        self.edition = edition
        self.sold_on = sold_on

    def sale_price(self):
        """Returns the sale price of the textbook as a float amount if not sold yet"""
        if self.sold_on is not None:
            return 'Already sold'
        else:
            return 50.0 * self.pages

    def purchase_price(self):
        """Returns the purchase price of the textbook as a float amount if it was already sold"""
        if self.sold_on is None:
            return 'Not yet sold'
        else:
            return 0.8 * self.initial_sale_price

    @abc.abstractmethod
    def book_type(self):
        """Returns a string representing the type of textbook this"""
        pass


class MathsBook(Textbook):
    """Class MathsBook inherits from Textbook"""
    initial_sale_price = 45000
    pages = 900

    def book_type(self):
        """Returns a string representing the type of textbook this"""
        return 'Maths book'


class EnglishBook(Textbook):
    """Class EnglishBook inherits from Textbook"""
    initial_sale_price = 9000
    pages = 800

    def book_type(self):
        """Returns a string representing the type of textbook this"""
        return 'English book'


class EconomicsBook(Textbook):
    """Class EconomicsBook inherits from Textbook"""
    initial_sale_price = 15000
    pages = 1000

    def book_type(self):
        """Returns a string representing the type of textbook this"""
        return 'Economics_book'
