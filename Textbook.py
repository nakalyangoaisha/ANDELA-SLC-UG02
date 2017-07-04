import abc


class Textbook(object):
    __metaclass__ = abc.ABCMeta
    initial_sale_price = 0
    pages = 0

    def __init__(self, year, author, edition, sold_on):
        self.year = year
        self.author = author
        self.edition = edition
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
            return 'Already sold'
        else:
            return 50 * self.pages

    def purchase_price(self):
        if self.sold_on is None:
            return 'Not yet sold'
        else:
            return 0.8 * self.initial_sale_price

    @abc.abstractmethod
    def book_type(self):
        pass
