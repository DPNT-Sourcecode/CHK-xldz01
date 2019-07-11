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
        discount = self.find_best_discount(quantity)

        if not discount:
            return self.original_price * quantity

        return (
            quantity % discount.quantity * self.original_price
            + discount.calculate_for(quantity)
        )

    def find_best_discount(self, quantity):
        if not self.discounts or quantity == 0:
            return None

        return self.discounts.get(quantity, self.find_best_discount(quantity - 1))


RULES = {
    "A": PricePolicy(50, [Discount(130, 3), Discount(120, 5)]),
    "B": PricePolicy(30, [Discount(45, 2)]),
    "C": PricePolicy(20),
    "D": PricePolicy(15),
    "E": PricePolicy(40),
}


def special_promo(basket, skuRequired, numSkuRequired, skuOffer, numSkuOffer):
    sku_apply_to = basket.get(skuRequired, 0)

    if sku_apply_to < numSkuRequired:
        return basket

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

    total = 0
    for sku, quantity in basket.items():
        total += RULES[sku].calculate_for(quantity)

    return round(total)




