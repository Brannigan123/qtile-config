from typing import List
from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .keyboard_bindings import MOD_KEY


MOUSE_DRAG_BINDINGS: List[Drag] = [
    Drag([MOD_KEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD_KEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]


MOUSE_FOCUS_BINDINGS: List[Click] = [
    Click([MOD_KEY], "Button2", lazy.window.bring_to_front())
]
