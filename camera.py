from dataclasses import replace

from constants import WIN_W, WIN_H, PLYR_W, PLYR_H, DEADZONE


def clamp_camera(camera_x, camera_y, world_width, world_height, zoom):
    """
    Keep the camera inside the world boundaries.

    camera_x and camera_y are in world coordinates.
    world_width and world_height are the full map size in pixels.
    """

    visible_width = WIN_W / zoom
    visible_height = WIN_H / zoom

    max_camera_x = world_width - visible_width
    max_camera_y = world_height - visible_height

    camera_x = max(0, min(camera_x, max_camera_x))
    camera_y = max(0, min(camera_y, max_camera_y))

    return camera_x, camera_y

def update_camera(state, camera_x, camera_y, player_world_x, player_world_y):

    zoom = state.camera.zoom

    dead_zone_width = WIN_W // DEADZONE
    dead_zone_height = WIN_H // DEADZONE

    box_left = (WIN_W - dead_zone_width) // 2
    box_right = box_left + dead_zone_width

    box_top = (WIN_H - dead_zone_height) // 2
    box_bottom = box_top + dead_zone_height


    player_screen_x, player_screen_y = world_to_screen(
                                                        player_world_x,
                                                        player_world_y,
                                                        state.camera
                                                        )

    player_screen_right = player_screen_x + PLYR_W * zoom
    player_screen_bottom = player_screen_y + PLYR_H * zoom

    # HORIZONTAL MOVEMENT
    if player_screen_x < box_left:
        camera_x = player_world_x - box_left / zoom

    elif player_screen_right > box_right:
        camera_x = (player_world_x + PLYR_W) - box_right/ zoom

    # VERTICAL MOVEMENT
    if player_screen_y < box_top:
        camera_y = player_world_y - box_top / zoom

    elif player_screen_bottom > box_bottom:
        camera_y = (player_world_y + PLYR_H) - box_bottom/ zoom

    # Clamp camera so it cannot show outside the map
    map_rows = len(state.game_map.tiles)
    map_cols = len(state.game_map.tiles[0])

    world_width = map_cols * state.game_map.tile_size
    world_height = map_rows * state.game_map.tile_size

    camera_x, camera_y = clamp_camera(
        camera_x,
        camera_y,
        world_width,
        world_height,
        zoom
    )

    new_camera = replace(state.camera, x=camera_x, y=camera_y)
    return replace(state, camera=new_camera)

def world_to_screen(world_x, world_y, camera):
    screen_x = (world_x - camera.x) * camera.zoom
    screen_y = (world_y - camera.y) * camera.zoom

    return screen_x, screen_y


