import csv


class ChocolatePromotionStrategy:
    def __init__(self, cash, price, ratio):
        self.cash = cash
        self.price = price
        self.ratio = ratio

    def calculate_quantity(self):
        quantity_purchased = self.cash // self.price

        return quantity_purchased


class MilkChocolatePromotion(ChocolatePromotionStrategy):
    def calculate_quantity(self):
        quantity_purchased = super().calculate_quantity()
        bonus_quantity = quantity_purchased // self.ratio
        total_quantity = quantity_purchased + bonus_quantity

        quantity = default_quantity.copy()
        quantity['milk'] = total_quantity

        return quantity


class VioletChocolatePromotion(ChocolatePromotionStrategy):
    def calculate_quantity(self):
        quantity_purchased = super().calculate_quantity()
        bonus_quantity = quantity_purchased // self.ratio
        total_quantity = quantity_purchased + (2 * bonus_quantity)

        quantity = default_quantity.copy()
        quantity['violet'] = total_quantity

        return quantity


class EspressoChocolatePromotion(ChocolatePromotionStrategy):
    def calculate_quantity(self):
        quantity_purchased = super().calculate_quantity()
        bonus_quantity = quantity_purchased // self.ratio
        total_quantity = quantity_purchased + bonus_quantity

        quantity = default_quantity.copy()
        quantity['espresso'] = total_quantity
        quantity['milk'] = total_quantity

        return quantity


class RubyChocolatePromotion(ChocolatePromotionStrategy):
    def calculate_quantity(self):
        quantity_purchased = super().calculate_quantity()
        bonus_packs = quantity_purchased // self.ratio
        bonus_quantity_per_type = bonus_packs * 2

        quantity = default_quantity.copy()
        quantity['milk'] = bonus_quantity_per_type
        quantity['violet'] = bonus_quantity_per_type,
        quantity['espresso'] = bonus_quantity_per_type,
        quantity['ruby'] = quantity_purchased

        return quantity


chocolate_types = {
    'milk': MilkChocolatePromotion,
    'violet': VioletChocolatePromotion,
    'espresso': EspressoChocolatePromotion,
    'ruby': RubyChocolatePromotion
}

default_quantity = {key: 0 for key in chocolate_types}


def load_orders(file_path):
    """Load and parse orders from the CSV file."""
    orders = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append({
                'type': row['type'],
                'cash': int(row['cash']),
                'price': int(row['price']),
                'ratio': int(row['ratio']),
            })
    print('ILGOR', orders)
    return orders


def calculate_chocolate_order(orders):
    results = []

    for order in orders:
        chocolate_type, cash, price, ratio = order['type'], order['cash'], order['price'], order['ratio']

        promotion_class = chocolate_types[chocolate_type]
        promotion = promotion_class(cash, price, ratio)

        quantities = promotion.calculate_quantity()
        results.append(quantities)

    return results


def generate_report(calculated_orders):
    """Generate a report of calculated chocolate orders."""
    for order in calculated_orders:
        print(order)


if __name__ == '__main__':
    orders = load_orders('input/orders.csv')

    calculated_orders = calculate_chocolate_order(orders)

    generate_report(calculated_orders)
