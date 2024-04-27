from gui_module.core import MainWindow
from gui_module.layouts import VerticalLayout
from gui_module.widgets import PrimaryButton

window = MainWindow("Example", (800, 600))
window.set_current_theme("dark")
layout = VerticalLayout()
fixed_button = PrimaryButton("Click")
fixed_button.set_fixed_size((100, 50))
fixed_button.pressed.connect(lambda: print("Button clicked"))
layout.add_widget(fixed_button)

button2 = PrimaryButton("Click")
layout.add_widget(button2)

window.set_layout(layout)
window.run()
