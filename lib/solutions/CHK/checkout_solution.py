class Discount:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_for(self, quantity):
        return quantity * self.price / self.quantity


class PricePolicy:
    def __init__(self, original_price, discount=None):
        self.original_price = original_price
        self.discount = discount

    def calculate_for(self, quantity):
        return self.original_price * quantity - self.discount_for(quantity)

    def discount_for(self, quantity):
        if not self.discount:
            return 0

        return self.discount.calculate_for(quantity)


RULES = {
    "A": PricePolicy(50, Discount(130, 3)),
    "B": PricePolicy(50, Discount(45, 2)),
    "C": PricePolicy(20),
    "D": PricePolicy(15),
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
        if i in basket:
            basket[i] += 1
        else:
            basket[i] = 1

    total = 0
    for sku, quantity in basket.items():
        total += RULES[sku].calculate_for(quantity)

    return round(total)

