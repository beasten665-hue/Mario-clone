import pygame
from constants import GROUND_TILE


def draw_tiles(screen, game_map):
    '''
    This simple function renders the platforms from the number in our TXT file
    :param screen: The screen to render to
    :param game_map: The TXT file for our level
    :return: None
    '''
    for row in range(len(game_map.tiles)):
        for col in range(len(game_map.tiles[row])):
            x = col * game_map.tile_size
            y = row * game_map.tile_size

            if game_map.tiles[row][col] == 1:
                pygame.draw.rect(screen,  GROUND_TILE,(x, y, game_map.tile_size, game_map.tile_size))
            pygame.draw.rect(screen, pygame.Color("black"), (x, y, game_map.tile_size, game_map.tile_size), 1)

def draw(screen, state):
    screen.fill('white')
    draw_tiles(screen, state.game_map)
    pygame.display.flip()