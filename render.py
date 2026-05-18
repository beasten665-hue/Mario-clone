import pygame

from camera import world_to_screen
from constants import GROUND_TILE, BASE_CLR, WIN_W, WIN_H, DEADZONE


def draw_dead_zone(screen):
    """
    Draw the camera dead zone rectangle on the screen.

    This is only for debugging so you can see when the camera should move.
    """

    dead_zone_width = WIN_W // DEADZONE
    dead_zone_height = WIN_H // DEADZONE

    box_left = (WIN_W - dead_zone_width) // 2
    box_top = (WIN_H - dead_zone_height) // 2

    pygame.draw.rect(
        screen,
        "red",
        (
            box_left,
            box_top,
            dead_zone_width,
            dead_zone_height
        ),
        2  # Border thickness only, not filled
    )

def draw_player(screen, player, camera):
    '''
    This simple function draw the player to the screen
    :param screen: Screen to be rendered to
    :param player: Player object to render
    :return: None
    '''

    screen_x, screen_y = world_to_screen(
                                                                player.x,
                                                                player.y,
                                                                camera
                                                            )

    pygame.draw.rect( screen,
                                BASE_CLR,
                     (screen_x,
                                screen_y,
                                player.width * camera.zoom,
                                player.height * camera.zoom)
                                )

def draw_tiles(screen, game_map, camera):
    '''
    This simple function renders the platforms from the number in our TXT file
    :param screen: The screen to render to
    :param game_map: The TXT file for our level
    :return: None
    '''
    for row_index, row in enumerate(game_map.tiles):
        for col_index, tile in enumerate(row):
            world_x = col_index * game_map.tile_size
            world_y = row_index * game_map.tile_size
            screen_x, screen_y = world_to_screen(world_x, world_y, camera)

            if game_map.tiles[row_index][col_index] == 1:
                pygame.draw.rect(screen,  GROUND_TILE,( screen_x,
                                                                                            screen_y,
                                                                                            game_map.tile_size * camera.zoom,
                                                                                            game_map.tile_size * camera.zoom))

            pygame.draw.rect(screen, pygame.Color("black"), (screen_x,
                                                                                                screen_y,
                                                                                                game_map.tile_size * camera.zoom,
                                                                                                game_map.tile_size * camera.zoom),
                                                                                    1)

def draw(screen, state):
    screen.fill('white')
    draw_tiles(screen, state.game_map, state.camera)
    draw_player(screen, state.player, state.camera)
    draw_dead_zone(screen)
    pygame.display.flip()