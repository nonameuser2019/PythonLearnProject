from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


if __name__ == '__main__':
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    print(queen_of_hearts.rank)
