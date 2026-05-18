from dataclasses import replace

from constants import PLYR_SPEED


def update_player_LnR(state,player):
    #Direction variable
    dx = 0

    #Add or subtract the player speed to the direction variable depending on the input
    if state.moving_left:
        dx -= PLYR_SPEED
    if state.moving_right:
        dx += PLYR_SPEED

    #Add the new direction variable to the player position
    new_x = player.x + dx

    #Don't forget to replace the state
    new_player = replace(player, x=new_x)
    return replace(state, player=new_player)