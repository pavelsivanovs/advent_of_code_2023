from dataclasses import dataclass
from enum import Enum
from io import TextIOWrapper
import math
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
        
        def __str__(self) -> str:
            return f'Set cubes: {self.red} red, {self.green} green, {self.blue} blue'
        
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
                setattr(game_set, color, int(amount))
            self.sets.append(game_set)        
          

def is_game_possible(game: Game) -> bool:
    for game_set in game.sets:
        if any([getattr(game_set, color.value, -1) > limits[color] for color in Color]):
            return False
    return True


def set_power(game_set: Game.Set) -> int:
    return math.prod([getattr(game_set, color.value, 0) for color in Color])


def minimum_game_power(game: Game) -> int:
    min_set = Game.Set()
    min_set.red = 0
    min_set.green = 0
    min_set.blue = 0
    
    for game_set in game.sets:
        for color in Color:
            if (set_val := getattr(game_set, color.value, 0)) > getattr(min_set, color.value, 0):
                setattr(min_set, color.value, set_val)
        
    return set_power(min_set)


def task_one(lines: TextIOWrapper) -> int:
    ids = []
    for line in lines:
        game = Game(line)
        if is_game_possible(game):
            ids.append(game.id)
    return sum(ids)


def task_two(lines: TextIOWrapper) -> int:
    game_powers = [minimum_game_power(Game(line)) for line in lines]
    return sum(game_powers)


if __name__ == '__main__':
    # print(minimum_game_power(Game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')))
    
    with open('input.txt', mode='r') as input_file:
        # print(task_one(input_file))
        print(task_two(input_file))
