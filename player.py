from dataclasses import replace

from collisions import rect_hits_wall, player_is_on_ground
from constants import PLYR_SPEED, PLYR_W, GRAVITY, JUMP_POWER, WIN_H


def update_player_jump(state):
    player = state.player

    if state.jump_pressed and  player.grounded:
       # print("JUMP CHECK", state.jump_pressed, state.player.grounded)
        new_player = replace(
            player,
            velocity_y=-JUMP_POWER,
            jumping=True,
            grounded=False
        )
        return replace(state, player=new_player, jump_pressed=False)
    return replace(state, jump_pressed=False)

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
    player_y = int(state.player.y)

    #storing the tile size into a variable
    tile_size = state.game_map.tile_size

    col = player_x // tile_size
    row = player_y// tile_size

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
    else:
        print("player is outside grid bounds")

    new_map = replace(state.game_map, tiles=tiles)
    return replace(state, game_map=new_map)

def update_player_gravity(state,player, game_map):
    player = state.player  # player object
    tile_size = state.game_map.tile_size  # Tile size
    floor_y = WIN_H - player.height  # The floor for the player of the window

    # standing on floor
    if player.y >= floor_y and player.velocity_y >= 0:
        new_player = replace(
            player,
            y=floor_y,
            velocity_y=0,
            grounded=True,
            jumping=False
        )
        return replace(state, player=new_player)

    # standing on tile
    if player.velocity_y >= 0 and player_is_on_ground(
            state.game_map,
            player.x,
            player.y,
            player.width,
            player.height
    ):
        snapped_y = (int((player.y + player.height) // tile_size) * tile_size) - player.height

        new_player = replace(
            player,
            y=snapped_y,
            velocity_y=0,
            grounded=True,
            jumping=False
        )
        return replace(state, player=new_player)

    # Every frame we add gravity to the players velocity
    velocity_y = player.velocity_y + GRAVITY
    # Then that vertical velocity is added to the player's y-position,
    # which makes the player move up or down over time.
    new_y = player.y + velocity_y

    # ----- floor collision first -----
    # If the players new Y_pos is greater than the set a new_player object
    if new_y >= floor_y:
        new_player = replace(
            player,
            y=floor_y,
            velocity_y=0,
            grounded=True,
            jumping=False
        )
        return replace(state, player=new_player)

    # ----- tile collision -----
    # If the one of the player corners hit a tile
    if rect_hits_wall(
            state.game_map,
            player.x,
            new_y,
            player.width,
            player.height
    ):
        # If the player is falling down
        if velocity_y > 0:
            plyr_bottom_edge = int(new_y + player.height - 1)
            # This finds the tile the bottom edge of the player is inside
            bottom_row = plyr_bottom_edge // tile_size
            # This finds the tile the bottom edge of the player is inside
            snapped_y = bottom_row * tile_size - player.height

            new_player = replace(
                player,
                y=snapped_y,
                velocity_y=0,
                grounded=True,
                jumping=False
            )
            return replace(state, player=new_player)

        # If the player is jumping up
        if velocity_y < 0:
            # Checks the position of the top edge of the square
            top_row = int(new_y // tile_size)
            snapped_y = (top_row + 1) * tile_size

            new_player = replace(
                player,
                y=snapped_y,
                velocity_y=0,
                grounded=False,
                jumping=True
            )
            return replace(state, player=new_player)

    # ----- normal air movement -----
    new_player = replace(
        player,
        y=new_y,
        velocity_y=velocity_y,
        grounded=False,
        jumping=True
    )
    return replace(state, player=new_player)

