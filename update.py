from camera import update_camera
from player import update_player_LnR, update_player_on_grid, update_player_gravity, update_player_jump


def update_game(state):
    state = update_player_LnR(state,state.player,state.game_map)
    state = update_player_gravity(state,state.player,state.game_map)
    state = update_player_on_grid(state)
    state = update_player_jump(state)
    state = update_camera(state, state.camera.x, state.camera.y, state.player.x, state.player.y)
    return state