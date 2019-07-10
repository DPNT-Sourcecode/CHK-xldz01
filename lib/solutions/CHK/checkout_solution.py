class Discount:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_for(self, quantity):
        return quantity * self.price / self.quantity



RULES = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    # scan the basket
    # return -1 if found invalid item
    for i in skus:
        if i not in RULES:
            return -1
        if i not in basket:
            basket[i] += 1
        else:
            basket[i] = 1

    raise NotImplementedError()


