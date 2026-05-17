import pygame
from constants import WIN_W, WIN_H
from input_handler import handle_event
from render import draw
from setup import make_initial_state
from update import update_game


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Enter name here")

    state = make_initial_state()

    while state.running:
        for event in pygame.event.get():
            state = handle_event(state,event)

        state = update_game(state)

        draw(screen, state)

        clock.tick(60)

if __name__ == '__main__':
    main()