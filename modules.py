from dataclasses import dataclass

@dataclass(frozen=True)
class GameMap:
    tiles: list[list[int]]
    tile_size: int
    width: int
    height: int

@dataclass(frozen=True)
class GameState:
    running: bool
    game_map: GameMap
