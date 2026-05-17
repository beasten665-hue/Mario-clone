import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Tower Combat")

    state = make_initial_state()

    while state.running:
        for event in pygame.event.get():
            state = handle_event(state,event)

        state = update_game(state)

        draw(screen, state)

        clock.tick(60)

if __name__ == '__main__':
    main()