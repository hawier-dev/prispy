import pygame

from prispy.core import Signal
from prispy.enums import CursorType


class Widget:
    def __init__(self, x=0, y=0, size=(100, 50)):
        self.x = x
        self.y = y
        self.size = size
        self.fixed_width = False
        self.fixed_height = False
        self.visible = True
        self.cursor = CursorType.ARROW
        self.is_hovered = False
        self.hover_started = Signal()
        self.hover_ended = Signal()

    def check_hover(self, mouse_pos):
        if (
            self.x <= mouse_pos[0] <= self.x + self.size[0]
            and self.y <= mouse_pos[1] <= self.y + self.size[1]
        ):
            if not self.is_hovered:
                self.is_hovered = True
                if self.cursor:
                    pygame.mouse.set_cursor(self.cursor.value)
                self.hover_started.emit()
        else:
            if self.is_hovered:
                self.is_hovered = False
                self.hover_ended.emit()

    def set_size(self, size):
        self.size = size

    def set_fixed_size(self, size):
        self.set_size(size)
        self.fixed_width = True
        self.fixed_height = True

    def set_cursor(self, cursor):
        self.cursor = cursor

    def check_if_hovered(self, mouse_pos):
        return (
            self.x <= mouse_pos[0] <= self.x + self.size[0]
            and self.y <= mouse_pos[1] <= self.y + self.size[1]
        )

    def set_fixed_width(self, width):
        self.size = (width, self.size[1])
        self.fixed_width = True

    def set_fixed_height(self, height):
        self.size = (self.size[0], height)
        self.fixed_height = True

    def handle_event(self, event):
        pass

    def render(self, surface, theme):
        pass

    def set_position(self, position):
        self.x, self.y = position

    def update(self, mouse_pos):
        self.check_hover(mouse_pos)
