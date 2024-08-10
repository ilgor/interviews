import unittest

from chocolate_promotion import (MilkChocolatePromotion, VioletChocolatePromotion,
                                 EspressoChocolatePromotion, RubyChocolatePromotion,
                                 calculate_chocolate_order, chocolate_types)


class TestChocolatePromotionStrategy(unittest.TestCase):

    def test_milk_chocolate_promotion(self):
        cash = 100
        price = 10
        ratio = 3
        promotion = MilkChocolatePromotion(cash, price, ratio)
        quantity = promotion.calculate_quantity()
        self.assertEqual(quantity, 13)  # (10 purchased + 3 bonus = 13 total)

    def test_violet_chocolate_promotion(self):
        cash = 120
        price = 15
        ratio = 4
        promotion = VioletChocolatePromotion(cash, price, ratio)
        quantity = promotion.calculate_quantity()
        # (8 purchased + 4*1=4 bonus = 12 total)
        self.assertEqual(quantity, 12)

    def test_espresso_chocolate_promotion(self):
        cash = 90
        price = 15
        ratio = 3
        promotion = EspressoChocolatePromotion(cash, price, ratio)
        espresso_quantity, bonus_quantity = promotion.calculate_quantity()
        self.assertEqual(espresso_quantity, 6)  # 6 purchased
        self.assertEqual(bonus_quantity, 2)  # 6 // 3 = 2 bonus packs

    def test_ruby_chocolate_promotion(self):
        cash = 120
        price = 20
        ratio = 4
        promotion = RubyChocolatePromotion(cash, price, ratio)
        quantities = promotion.calculate_quantity()
        expected_quantities = {
            'milk': 6,
            'violet': 6,
            'espresso': 6,
            'ruby': 6
        }
        self.assertEqual(quantities, expected_quantities)

    def test_calculate_chocolate_order(self):
        orders = [
            {
                'type': 'milk',
                'cash': 100,
                'price': 10,
                'ratio': 3,
            },
            {
                'type': 'violet',
                'cash': 120,
                'price': 15,
                'ratio': 4,
            },
            {
                'type': 'espresso',
                'cash': 90,
                'price': 15,
                'ratio': 3,
            },
            {
                'type': 'ruby',
                'cash': 120,
                'price': 20,
                'ratio': 4,
            },
        ]

        calculated_orders = calculate_chocolate_order(orders)

        expected_results = [
            'milk 13, milk 0, violet 0, espresso 0',
            'violet 12, milk 0, violet 0, espresso 0',
            'espresso 6, milk 2, violet 0',
            'milk 6, violet 6, espresso 6, ruby 6',
        ]

        self.assertEqual(calculated_orders, expected_results)


if __name__ == '__main__':
    unittest.main()
