import pygame


class ButtonStyle:
    def __init__(self, font_name, font_size, text_color, background_color, hover_color, pressed_color, border_radius):
        self.font = pygame.font.Font(font_name, font_size)
        self.text_color = text_color
        self.background_color = background_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.border_radius = border_radius

