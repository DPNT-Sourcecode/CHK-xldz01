class Discount:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_for(self, quantity):
        return quantity // self.quantity * self.price


class PricePolicy:
    def __init__(self, original_price, discounts=None):
        self.original_price = original_price
        self.discounts = self.discount_mapping(discounts)

    def discount_mapping(self, discounts):
        if not discounts:
            return {}

        temp = {}
        for discount in discounts:
            temp[discount.quantity] = discount
        return temp

    def calculate_for(self, quantity):
        price = 0
        tracking_quantity = quantity
        discount = self.find_best_discount(quantity)
        while discount:
            price += discount.price
            tracking_quantity -= discount.quantity
            discount = self.find_best_discount(tracking_quantity)

        price += tracking_quantity * self.original_price
        return price

    def find_best_discount(self, quantity):
        if not self.discounts or quantity == 0:
            return None

        return self.discounts.get(quantity, self.find_best_discount(quantity - 1))


RULES = {
    "A": PricePolicy(50, [Discount(130, 3), Discount(200, 5)]),
    "B": PricePolicy(30, [Discount(45, 2)]),
    "C": PricePolicy(20),
    "D": PricePolicy(15),
    "E": PricePolicy(40),
    "F": PricePolicy(10),
    "G": PricePolicy(20),
    "H": PricePolicy(10, [Discount(45, 5), Discount(80, 10)]),
    "I": PricePolicy(35),
    "J": PricePolicy(60),
    "K": PricePolicy(70, [Discount(120, 2)]),
    "L": PricePolicy(90),
    "M": PricePolicy(15),
    "N": PricePolicy(40),
    "O": PricePolicy(10),
    "P": PricePolicy(50, [Discount(200, 5)]),
    "Q": PricePolicy(30, [Discount(80, 3)]),
    "R": PricePolicy(50),
    "S": PricePolicy(20),
    "T": PricePolicy(20),
    "U": PricePolicy(40),
    "V": PricePolicy(50, [Discount(90, 2), Discount(130, 3)]),
    "W": PricePolicy(20),
    "X": PricePolicy(17),
    "Y": PricePolicy(20),
    "Z": PricePolicy(21),
}


def special_promo(basket, skuRequired, numSkuRequired, skuOffer, numSkuOffer):
    sku_apply_to = basket.get(skuRequired, 0)
    num_offer_applicable = sku_apply_to // numSkuRequired

    if sku_apply_to < numSkuRequired:
        return basket

    for _ in range(num_offer_applicable):
        sku_get_offer = basket.get(skuOffer, 0)
        if sku_get_offer < numSkuOffer:
            return basket
        basket[skuOffer] -= numSkuOffer

    return basket


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

    special_promo(basket, "E", 2, "B", 1)
    special_promo(basket, "F", 3, "F", 1)
    special_promo(basket, "N", 3, "M", 1)
    special_promo(basket, "R", 3, "Q", 1)
    special_promo(basket, "U", 4, "U", 1)

    total = 0
    for sku, quantity in basket.items():
        total += RULES[sku].calculate_for(quantity)

    return round(total)


