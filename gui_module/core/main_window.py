import pygame
import sys


class MainWindow:
    def __init__(self, title, size):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.running = True
        self.main_widget = None

    def set_main_widget(self, widget):
        self.main_widget = widget

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.main_widget:
                    self.main_widget.handle_event(event)

            self.screen.fill((255, 255, 255))
            if self.main_widget:
                self.main_widget.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()