import pygame
from dataclasses import replace

def handle_event(state, event):
    if event.type == pygame.QUIT:
        return replace(state, running=False)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return replace(state, moving_left=True)
        if event.key == pygame.K_RIGHT:
            return replace(state, moving_right=True)
        if event.key == pygame.K_SPACE:
            return replace(state, jump_pressed = True)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            return replace(state, moving_left=False)
        if event.key == pygame.K_RIGHT:
            return replace(state, moving_right=False)

    return state