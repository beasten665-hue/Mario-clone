from constants import WIN_W, WIN_H, PLYR_W, PLYR_H, TILE_SIZE, ZOOM
from modules import GameState, GameMap, Player, Camera


def load_level(filename):
    '''
    This simple function reads the file of our level that we created
    :param filename: The name of the file for the level
    :return: The 2D matrix of tiles
    '''

    #Here we are opening the desired file
    with open(filename,'r') as file:
        lines = file.readlines()

    #List to store our rows of chars
    tiles = []

    #Looping through the file to read the rows
    for line in lines:
        row = [] #Storing the rows

        #Looping through each char and striping spaces
        for char in line.strip():
            row.append(int(char))#Putting the stripped char into the row list
        tiles.append(row) #After looping though the entire row of chars append to the row to tiles list

    return tiles


def make_initial_state():

    tiles = load_level('C:\\Users\\user\\Desktop\\Mario Clone\\Levels\\level1.txt')

    player = Player(
        x=0,
        y=0,
        width=PLYR_W,
        height=PLYR_H,
        jumping=False,
        grounded=False,
        velocity_y=0
    )

    camera = Camera(
        x=player.x,
        y=player.y,
        zoom=ZOOM,

    )
    game_map = GameMap(
        tiles = tiles, #Map notepad file
        tile_size = TILE_SIZE,
    )

    return GameState(
        running=True,
        game_map = game_map,
        camera = camera,
        player = player,
        moving_left=False,
        moving_right=False,
        jump_pressed=False,

    )