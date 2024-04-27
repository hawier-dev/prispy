class Layout:
    def __init__(self, spacing=5):
        self.widgets = []
        self.parent_size = (0, 0)
        self.spacing = spacing
        self.padding = 5

    def set_spacing(self, spacing):
        self.spacing = spacing

    def set_padding(self, padding):
        self.padding = padding

    def add_widget(self, widget):
        self.widgets.append(widget)

    def set_parent_size(self, size):
        self.parent_size = size
