import pygame
from dataclasses import replace

def handle_event(state, event):
    if event.type == pygame.QUIT:
        return replace(state, running=False)
    return state