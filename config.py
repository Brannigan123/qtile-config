from typing import List
from libqtile.config import Key, Mouse, Screen, hook
from libqtile.bar import Gap
from b_theme import load_theme, load_wallpaper_path
from shortcut_bindings import *
from layouts import DEFAULT_LAYOUT_BEHAVIOUR, FLOATING_TYPES, build_floating_layout, build_layouts
from lifecycle import clean_up, set_floating_windows, startup_daemons
from topbar import build_topbar
from workspaces import GROUPS, get_monitors
import apps


mod = MOD_KEY
wmname = "qtile"
terminal = apps.TERMINAL

reconfigure_screens = True
theme = load_theme()

groups = GROUPS
floating_types = FLOATING_TYPES
layout_behaviour = DEFAULT_LAYOUT_BEHAVIOUR
layouts = build_layouts(theme.colors, theme.measurements, layout_behaviour)
floating_layout = build_floating_layout(
    theme.colors, theme.measurements, layout_behaviour)

keys: List[Key] = [
    *QTILE_BINDINGS,
    *GROUP_SWITCHING_BINDINGS,
    *WINDOW_GROUP_SWITCHING_BINDINGS,
    *WINDOW_CONTROL_BINDINGS,
    *WINDOW_FOCUS_BINDINGS,
    *WINDOW_RESIZE_BINDINGS,
    *WINDOW_MOVEMENT_BINDINGS,
    *COMMON_GUI_BINDINGS,
    *SCREEN_CAPTURE_BINDINGS,
    *SCREEN_BRIGHTNESS_BINDINGS,
    *AUDIO_LEVEL_BINDINGS,
    *MEDIA_PLAYER_BINDINGS,
]

mouse: List[Mouse] = [
    *MOUSE_DRAG_BINDINGS,
    *MOUSE_FOCUS_BINDINGS,
]

screens = [
    Screen(
        wallpaper=load_wallpaper_path(theme.wallpaper.path),
        wallpaper_mode='stretch' if theme.wallpaper.stretch else 'fill',
        top=build_topbar(monitor, theme, theme.measurements),
        right=Gap(theme.measurements.margin),
        left=Gap(theme.measurements.margin),
        bottom=Gap(theme.measurements.margin),
    )
    for monitor in get_monitors()
]

widget_defaults = dict(
    font=theme.fonts.font0,
    fontsize=theme.fonts.font0_size,
    padding=theme.measurements.padding,
    margin=theme.measurements.margin,
    border_width=theme.measurements.border_width,
    background=theme.colors.background,
    foreground=theme.colors.foreground,
)

extension_defaults = widget_defaults.copy()

follow_mouse_focus = layout_behaviour.follow_mouse_focus
bring_front_click = layout_behaviour.bring_front_click
cursor_warp = layout_behaviour.cursor_warp
focus_on_window_activation = "smart"
auto_fullscreen = layout_behaviour.auto_fullscreen
auto_minimize = layout_behaviour.auto_minimize

dgroups_key_binder: None = None
dgroups_app_rules: List = []


@hook.subscribe.startup_once
def on_first_startup():
    startup_daemons()


@hook.subscribe.restart
def on_restart():
    clean_up()


@hook.subscribe.shutdown
def on_shutdown():
    clean_up()


@hook.subscribe.client_new
def on_new(window):
    set_floating_windows(window)
