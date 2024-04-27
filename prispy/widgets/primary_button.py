import pygame

from prispy.core import Signal
from prispy.enums import CursorType
from prispy.styles import ButtonStyle
from prispy.widgets import Widget


class PrimaryButton(Widget):
    def __init__(self, text, x=0, y=0, size=(100, 50), style=None):
        super().__init__(x, y, size)
        self._is_pressed = False
        self.text = text
        self.font = pygame.font.Font(None, 36)

        self.pressed = Signal()

        self.set_cursor(CursorType.POINTER)

    def render(self, surface, theme):
        style = theme.primary_button_style
        if self.visible:
            background_color = style.background_color
            if self.is_hovered:
                background_color = style.hover_color
            if self._is_pressed:
                background_color = style.pressed_color

            pygame.draw.rect(
                surface,
                background_color,
                (self.x, self.y, *self.size),
                border_radius=style.border_radius,
            )

            text_surface = style.font.render(
                self.text, True, style.text_color
            )
            text_rect = text_surface.get_rect(
                center=(self.x + self.size[0] // 2, self.y + self.size[1] // 2)
            )
            surface.blit(text_surface, text_rect)

    def set_text(self, new_text):
        self.text = new_text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_if_hovered(pygame.mouse.get_pos()):
                self._is_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._is_pressed and self.check_if_hovered(pygame.mouse.get_pos()):
                self._is_pressed = False
                self.pressed.emit()
        elif event.type == pygame.MOUSEMOTION:
            self._is_pressed = (
                self.check_if_hovered(pygame.mouse.get_pos()) and self._is_pressed
            )
