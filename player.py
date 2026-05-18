from dataclasses import replace

from collisions import rect_hits_wall
from constants import PLYR_SPEED, PLYR_W


def update_player_LnR(state, player, game_map):
    '''
    This fucntion only moves the player left and right on the screen
    :param state: The current state of the program
    :param player: The current state of the player
    :return: Return the new state with the old state
    '''
    #Direction variable
    dx = 0

    #Add or subtract the player speed to the direction variable depending on the input
    if state.moving_left:
        dx -= PLYR_SPEED
    if state.moving_right:
        dx += PLYR_SPEED

    #Add the new direction variable to the player position
    new_x = player.x + dx

    if rect_hits_wall(
        game_map,
        new_x,
        player.y,
        player.width,
        player.height
    ):
        return state

    #Don't forget to replace the state
    new_player = replace(player, x=new_x)
    return replace(state, player=new_player)

def update_player_on_grid(state):
    '''
    This function puts the player position from the screen to the logical
    grid on the map
    :param state: The current state of the game
    :return: Return the new state of the game with updated position
    '''
    #Getting the player center position
    player_x = int(state.player.x)
    player_center = int(player_x + PLYR_W /2)

    #storing the tile size into a variable
    tile_size = state.game_map.tile_size

    col = player_center // tile_size
    row = player_center // tile_size

    #Getting a copy of the game map tiles
    tiles = [r[:] for r in state.game_map.tiles]

    # clear old p markers first by looping through the copy
    for r in range(len(tiles)):
        for c in range(len(tiles[r])):
            if tiles[r][c] == 'p':
                tiles[r][c] = 0

    # bounds checking to make sure the player doesn't go beyond the list
    if 0 <= row < len(tiles) and 0 <= col < len(tiles[row]):
        tiles[row][col] = 'p'
        print(tiles)
    else:
        print("player is outside grid bounds")

    new_map = replace(state.game_map, tiles=tiles)
    return replace(state, game_map=new_map)