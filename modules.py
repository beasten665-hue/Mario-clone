from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    x: int
    y: int
    width: int
    height: int
    jumping: bool
    velocity_y: int
    grounded: bool

@dataclass(frozen=True)
class Camera:
    x: int
    y: int
    zoom: int

@dataclass(frozen=True)
class GameMap:
    tiles: list[list[int]]
    tile_size: int

@dataclass(frozen=True)
class GameState:
    running: bool
    game_map: GameMap
    player: Player
    moving_left: bool
    moving_right: bool
    jump_pressed: bool
    camera: Camera

