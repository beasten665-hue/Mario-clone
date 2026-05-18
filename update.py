from player import update_player_LnR


def update_game(state):
    state = update_player_LnR(state,state.player)
    return state