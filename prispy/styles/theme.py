import pygame

from prispy.styles import ButtonStyle


class Theme:
    def __init__(
        self,
        font_name="",
        primary_color=(0, 123, 255),
        secondary_color=(255, 193, 7),
        background_color=(250, 250, 250),
        on_primary_color=(255, 255, 255),
        on_secondary_color=(0, 0, 0),
        primary_button_style=None,
        secondary_button_style=None,
    ):
        self.font_name = font_name
        if not self.font_name:
            self.font_name = pygame.font.get_default_font()
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.background_color = background_color
        self.on_primary_color = on_primary_color
        self.on_secondary_color = on_secondary_color

        if not primary_button_style:
            primary_hover_color = (
                min(primary_color[0] + 20, 255),
                min(primary_color[1] + 20, 255),
                min(primary_color[2] + 20, 255),
            )
            primary_pressed_color = (
                max(primary_color[0] - 20, 0),
                max(primary_color[1] - 20, 0),
                max(primary_color[2] - 20, 0),
            )

            primary_button_style = ButtonStyle(
                font_name=self.font_name,
                font_size=16,
                text_color=on_primary_color,
                background_color=primary_color,
                hover_color=primary_hover_color,
                pressed_color=primary_pressed_color,
                border_radius=5,
            )
        self.primary_button_style = primary_button_style

        if not secondary_button_style:
            secondary_hover_color = (
                min(secondary_color[0] + 20, 255),
                min(secondary_color[1] + 20, 255),
                min(secondary_color[2] + 20, 255),
            )
            secondary_pressed_color = (
                max(secondary_color[0] - 20, 0),
                max(secondary_color[1] - 20, 0),
                max(secondary_color[2] - 20, 0),
            )

            secondary_button_style = ButtonStyle(
                font_name=self.font_name,
                font_size=16,
                text_color=on_secondary_color,
                background_color=secondary_color,
                hover_color=secondary_hover_color,
                pressed_color=secondary_pressed_color,
                border_radius=5,
            )
        self.secondary_button_style = secondary_button_style


    @classmethod
    def dark(cls):
        return cls(
            primary_color=(0, 123, 255),
            secondary_color=(255, 193, 7),
            background_color=(11, 11, 11),
            on_primary_color=(255, 255, 255),
            on_secondary_color=(0, 0, 0),
        )

    @classmethod
    def light(cls):
        return cls(
            primary_color=(0, 123, 255),
            secondary_color=(255, 193, 7),
            background_color=(250, 250, 250),
            on_primary_color=(255, 255, 255),
            on_secondary_color=(0, 0, 0),
        )