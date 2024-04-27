import pygame

from gui_module.enums import CursorType
from gui_module.styles import Theme


class MainWindow:
    def __init__(self, title, size):
        pygame.init()
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.layout = None
        self.size = size
        self._default_cursor = CursorType.ARROW
        self.light_theme = Theme()
        self.dark_theme = Theme.dark()
        self._theme = self.light_theme

    def set_light_theme(self, theme):
        self.light_theme = theme

    def set_dark_theme(self, theme):
        self.dark_theme = theme

    def set_current_theme(self, theme: str):
        if theme == 'light':
            self._theme = self.light_theme
        elif theme == 'dark':
            self._theme = self.dark_theme

    def set_layout(self, layout):
        self.layout = layout
        self.layout.set_parent_size(self.size)

    def set_default_cursor(self, cursor: CursorType):
        self._default_cursor = cursor

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            any_hovered = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.size = event.size
                    self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
                    if self.layout:
                        self.layout.set_parent_size(self.size)
                else:
                    for widget in self.layout.widgets:
                        widget.handle_event(event)

            self.screen.fill(self._theme.background_color)

            if self.layout:
                self.layout.layout_widgets()
                for widget in self.layout.widgets:
                    widget.update(mouse_pos)
                    widget.render(self.screen, self._theme)
                    if widget.is_hovered:
                        any_hovered = True

            if not any_hovered:
                pygame.mouse.set_cursor(self._default_cursor.value)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
