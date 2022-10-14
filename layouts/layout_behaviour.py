from dataclasses import dataclass


@dataclass
class LayoutBehavior:
    fair: bool 
    border_on_single: bool 
    margin_on_single: bool 
    grow_amount: int 
    windows_ratio: float 
    aspect_ratio: float 
    ratio_increment: float 
    wrap_clients: bool 
    follow_mouse_focus: bool 
    bring_front_click: bool 
    cursor_warp: bool 
    auto_fullscreen: bool 
    auto_minimize: bool 

DEFAULT_LAYOUT_BEHAVIOUR = LayoutBehavior(
    fair = True,
    border_on_single = True,
    margin_on_single = True,
    grow_amount = 5,
    windows_ratio = 0.6180469715698392,
    aspect_ratio = 1.618,
    ratio_increment = 0.05,
    wrap_clients = True,
    follow_mouse_focus = True,
    bring_front_click = True,
    cursor_warp = False,
    auto_fullscreen = True,
    auto_minimize = True,
)