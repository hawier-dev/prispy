import pygame
from enum import Enum


class CursorType(Enum):
    ARROW = pygame.SYSTEM_CURSOR_ARROW
    TEXT = pygame.SYSTEM_CURSOR_IBEAM
    POINTER = pygame.SYSTEM_CURSOR_HAND
