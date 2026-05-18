from player import update_player_LnR, update_player_on_grid


def update_game(state):
    state = update_player_LnR(state,state.player,state.game_map)
    state = update_player_on_grid(state)
    return state