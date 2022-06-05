class Warrior:
    def __init__(self, level=1, experience=100, rank='Pushover'):
        self.level = level
        self.experience = experience
        self.rank = rank

    def fight(self, enemy_lvl):
        if enemy_lvl < 1 or enemy_lvl > 100:
            return 'Invalid level'
        if enemy_lvl - self.level == 0:
            self.experience += 10
        elif enemy_lvl - self.level == -1:
            self.experience += 5
        elif enemy_lvl - self.level <= -5:
            pass




    def __repr__(self):
        return f'level: {self.level}, experience: {self.experience}, rank: {self.rank}'


if __name__ == '__main__':
    tom = Warrior()
    assert tom.level == 1
    assert tom.experience == 100
    assert tom.rank == "Pushover"

    assert tom.fight(0) == 'Invalid level'
    assert tom.fight(101) == 'Invalid level'