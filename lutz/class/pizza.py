class Pizza:

    order_number = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'oilives', 'mushroom'])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    def __str__(self):
        return f'{self.ingr}'


if __name__ == '__main__':
    p1 = Pizza(['bacon', 'parmezan', 'ham'])
    print(p1.ingredients)
    p2 = Pizza.meat_festival()
    print(p2.ingredients)
    print(p1.order_number)
    print(p2.order_number)
    print(Pizza.order_number)
