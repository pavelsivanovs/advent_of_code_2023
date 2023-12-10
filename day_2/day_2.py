from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
from typing import Optional


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


limits = {
    Color.RED: 12, 
    Color.GREEN: 13,
    Color.BLUE: 14
}


@dataclass
class Game:
    class Set:
        red: Optional[int]
        green: Optional[int]
        blue: Optional[int]
    id: int
    sets: list[Set]
    
    def __init__(self, init_str: str):
        game_str, set_strs = init_str.split(':')
        self.id = int(game_str.split()[1])
        
        self.sets = []
        for set_str in set_strs.split(';'):
            game_set = self.Set()
            for color_str in set_str.split(','):
                amount, color = tuple(color_str.strip().split())
                game_set.__setattr__(color, int(amount))
            self.sets.append(game_set)        
          

def is_game_possible(game: Game) -> bool:
    for game_set in game.sets:
        if any([getattr(game_set, color.value, -1) > limits[color] for color in Color]):
            return False
    return True


def main(lines: TextIOWrapper) -> int:
    ids = []
    for line in lines:
        game = Game(line)
        if is_game_possible(game):
            ids.append(game.id)
    return sum(ids)


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_file:
        print(main(input_file))
