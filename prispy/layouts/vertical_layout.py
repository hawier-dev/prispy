from prispy.layouts.layout import Layout


class VerticalLayout(Layout):
    def __init__(self, spacing=5):
        super().__init__(spacing)

    def layout_widgets(self):
        current_y = self.padding
        total_height = self.parent_size[1] - 2 * self.padding

        total_fixed_height = sum(widget.size[1] for widget in self.widgets if widget.fixed_height)
        total_spacing = self.padding * (len(self.widgets) - 1)
        available_height = total_height - total_fixed_height - total_spacing
        count_dynamic_widgets = sum(1 for widget in self.widgets if not widget.fixed_height)
        dynamic_height = available_height / count_dynamic_widgets if count_dynamic_widgets > 0 else 0

        for widget in self.widgets:
            if widget.fixed_width:
                width = widget.size[0]
            else:
                width = self.parent_size[0] - 2 * self.padding

            if widget.fixed_height:
                height = widget.size[1]
            else:
                height = dynamic_height

            widget.set_size((width, height))
            widget.set_position((self.padding, current_y))

            current_y += height + self.padding

