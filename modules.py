from dataclasses import dataclass


@dataclass(frozen=True)
class GameState:
    running: bool