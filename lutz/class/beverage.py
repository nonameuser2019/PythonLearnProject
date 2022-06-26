class Beverage:
    prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def cost(self):
        cost = 0
        for ing in self.ingredients:
            cost += Beverage.prices.get(ing, 0)
        return cost

    def get_cost(self):
        return f'${self.cost():.2f}'

    def get_price(self):
        price = self.cost() * 2.5
        return f'${price:.2f}'

    def get_name(self):
        sorted_ing = sorted(self.ingredients)
        if len(self.ingredients) > 1:
            return ' '.join(sorted_ing).replace('berries', 'berry') + ' Fusion'
        return ' '.join(sorted_ing).replace('berries', 'berry') + ' Smoothie'

    def __str__(self):
        return f'{self.ingredients}'


if __name__ == '__main__':
    b1 = Beverage(['Banana', 'Mango'])
    b2 = Beverage(['Blueberries'])
    b3 = Beverage(['Blueberries', 'Banana'])
    print(b2.get_name())
    print(b1.get_price())
    print(b3.get_price())
    print(b1.get_cost())
    print(b3.get_name())
