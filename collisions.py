def is_wall(game_map, row, col):
    """
        Determine whether a tile position in the map should be treated as a wall.

        This helper checks a grid-based map using a row and column index and returns
        True when the requested tile is solid or when the position is outside the
        valid bounds of the map.

        Behavior:
        - Returns True if `row` is less than 0 or greater than the last valid row.
        - Returns True if `col` is less than 0 or greater than the last valid
          column for that row.
        - Returns True if the tile value at `game_map.tiles[row][col]` is equal to 1.
        - Returns False for any in-bounds tile whose value is not 1.

        This design is useful for collision systems because it allows out-of-bounds
        positions to be treated as solid walls, preventing the player or other
        objects from moving off the map.

        Args:
            game_map: The map object that contains:
                - `tiles`: a 2D list representing the map grid
                - `tile_size`: the size of one tile in pixels (not used directly
                  in this function, but typically part of the same map structure)
            row (int): The row index of the tile to check.
            col (int): The column index of the tile to check.

        Returns:
            bool:
                - True if the given position is out of bounds or contains a wall tile
                  represented by the value `1`.
                - False if the given position is inside the map and is not a wall.

        Example:
            game_map.tiles = [
                [0, 0, 1],
                [0, 1, 0],
                [0, 0, 0]
            ]

            is_wall(game_map, 0, 2)   # True  -> tile value is 1
            is_wall(game_map, 2, 1)   # False -> tile value is 0
            is_wall(game_map, -1, 0)  # True  -> out of bounds
            is_wall(game_map, 1, 99)  # True  -> out of bounds

        Notes:
            - This function assumes that the value `1` represents a solid wall tile.
            - If your map uses a different value for walls, update the final return
              statement accordingly.
            - Treating out-of-bounds positions as walls is a common and convenient
              approach in tile-based collision systems.
        """
    #These two conditions below check weather row and col are outside the map
    if row < 0 or row >= len(game_map.tiles):
        #We return True so that if the player is outside the map
        #it will block the players movement
        return True
    if col < 0 or col >= len(game_map.tiles[row]):
        return True

    #This check if the tile position on the grid is a actual wall we clicked
    return game_map.tiles[row][col] == 1

def rect_hits_wall(game_map,rect_x,rect_y,width,height):
    """
        Check whether a rectangle overlaps any wall tile in a grid-based map.

        This function is used for tile collision detection. It takes a rectangle
        described in pixel coordinates and determines whether any of the tiles
        touched by the rectangle's four corners should be treated as walls.

        The rectangle exists in pixel space, while the map exists in tile space.
        Because of that, the function first converts the rectangle's outer edges
        into tile row and column positions. It then builds the four corner tile
        positions and checks each one with `is_wall()`.

        A collision is reported if any one of the corner tiles:
        - is outside the valid bounds of the map, or
        - contains a wall tile represented by the value `1`

        Corner order checked:
        - top-left
        - top-right
        - bottom-left
        - bottom-right

        Args:
            game_map: The map object containing:
                - `tiles`: a 2D list representing the tile grid
                - `tile_size`: the width and height of each tile in pixels
            x (int | float): The x-coordinate of the rectangle's left edge in pixels.
            y (int | float): The y-coordinate of the rectangle's top edge in pixels.
            width (int): The width of the rectangle in pixels.
            height (int): The height of the rectangle in pixels.

        Returns:
            bool:
                - True if any corner of the rectangle is inside a wall tile or
                  outside the map bounds.
                - False if all four corners are inside valid, non-wall tiles.

        How it works:
            1. Read the map's tile size.
            2. Convert the rectangle's left and right pixel edges into tile columns.
            3. Convert the rectangle's top and bottom pixel edges into tile rows.
            4. Store the four corner tile positions in a list.
            5. Loop through each corner position.
            6. Use `is_wall()` to determine whether that tile is solid.
            7. Return True immediately if any corner hits a wall.
            8. Return False if no corner collides.

        Notes:
            - `x + width - 1` and `y + height - 1` are used so the right and bottom
              edges stay inside the rectangle's actual occupied space.
            - This function checks the tiles containing the rectangle's corners, not
              every tile the full rectangle may cover.
            - This method works well for many simple tile-based games, especially
              when movement speed is moderate and the object is not extremely large.
            - For larger objects or more advanced collision systems, checking only
              the corners may not always be enough.

        Example:
            If `tile_size = 40` and the rectangle is at:
                x = 85, y = 70, width = 50, height = 30

            Then the function computes:
                left_col   = 85 // 40 = 2
                right_col  = (85 + 50 - 1) // 40 = 3
                top_row    = 70 // 40 = 1
                bottom_row = (70 + 30 - 1) // 40 = 2

            Corner tiles checked:
                (1, 2), (1, 3), (2, 2), (2, 3)

            If any of those tiles are walls, the function returns True.
        """
    tile_size = game_map.tile_size

    #These variables determine the position of the rectangles edges
    #and which tile they are in.
    left_col = int(rect_x) // tile_size
    right_col = int(rect_x + width - 1) // tile_size
    top_row = int(rect_y) // tile_size
    bottom_row = int(rect_y+height -1 ) // tile_size

    #The points below are the corner points of the rectangle
    corners = [(top_row, left_col),
               (top_row, right_col),
               (bottom_row, left_col),
               (bottom_row, right_col)
                ]

    #This loops over the list of corners list and uses the is_wall function to check collision
    for row, col in corners:
        if is_wall(game_map, row, col):
            return True
    return False