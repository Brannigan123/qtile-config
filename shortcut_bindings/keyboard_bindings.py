from typing import List
from libqtile.config import Key
from libqtile.lazy import lazy
from workspaces import GROUPS
from apps import TERMINAL
import os.path as path


HOME_DIR = path.expanduser("~")
MOD_KEY: str = 'Mod4'


QTILE_BINDINGS: List[Key] = [
    Key([MOD_KEY, "shift"], "Tab", lazy.next_layout(),
        desc="toggle between layouts"),
    Key([MOD_KEY, "shift"], "c",
        lazy.reload_config(), desc="reload the config"),
    Key([MOD_KEY, "shift"], "r",
        lazy.restart(), desc="restart qtile"),
    Key([MOD_KEY, "shift"], "q", lazy.shutdown(), desc="shutdown qtile"),
    Key([MOD_KEY, "shift"], "x", lazy.spawn(
        "betterlockscreen -s"), desc="suspend session & lock screen"),
]

GROUP_SWITCHING_BINDINGS: List[Key] = [
    Key(
        [MOD_KEY],
        group.name,
        lazy.group[group.name].toscreen(),
        desc=f"switch to group {group.name}",
    )
    for group in GROUPS
]


WINDOW_GROUP_SWITCHING_BINDINGS: List[Key] = [
    Key(
        [MOD_KEY, "shift"],
        group.name,
        lazy.window.togroup(group.name, switch_group=True),
        desc=f"move focused window to & switch to group {group.name}",
    )
    for group in GROUPS
]


WINDOW_CONTROL_BINDINGS: List[Key] = [
    Key([MOD_KEY], "q", lazy.window.kill(), desc="kill focused window"),
    Key([MOD_KEY], "r", lazy.layout.normalize(),
        desc="reset all window sizes"),
    Key([MOD_KEY], "f", lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen mode on focused window"),
]


WINDOW_FOCUS_BINDINGS: List[Key] = [
    Key([MOD_KEY], "Left", lazy.layout.left(), desc="move focus to left"),
    Key([MOD_KEY], "Right", lazy.layout.right(), desc="move focus to right"),
    Key([MOD_KEY], "Down", lazy.layout.down(), desc="move focus down"),
    Key([MOD_KEY], "Up", lazy.layout.up(), desc="move focus up"),
    Key([MOD_KEY], "Tab", lazy.layout.next(),
        desc="move window focus to the next window"),
]


WINDOW_RESIZE_BINDINGS: List[Key] = [
    Key([MOD_KEY, "control"], "Left", lazy.layout.grow_left(),
        desc="grow window to the left"),
    Key([MOD_KEY, "control"], "Right", lazy.layout.grow_right(),
        desc="grow window to the right"),
    Key([MOD_KEY, "control"], "Down",
        lazy.layout.grow_down(), desc="grow window down"),
    Key([MOD_KEY, "control"], "Up",
        lazy.layout.grow_up(), desc="grow window up"),
]


WINDOW_MOVEMENT_BINDINGS: List[Key] = [
    Key([MOD_KEY, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="move window to the left"),
    Key([MOD_KEY, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="move window to the right"),
    Key([MOD_KEY, "shift"], "Down",
        lazy.layout.shuffle_down(), desc="move window down"),
    Key([MOD_KEY, "shift"], "Up",
        lazy.layout.shuffle_up(), desc="move window up"),
]


COMMON_GUI_BINDINGS: List[Key] = [
    Key([MOD_KEY], "space", lazy.spawn("rofi -show drun"),
        desc="Show appliction menu widget"),
    Key([MOD_KEY], "Return", lazy.spawn(TERMINAL),
        desc="Launch a terminal window"),
]


SCREEN_CAPTURE_BINDINGS: List[Key] = [
    Key([], "Print", lazy.spawn(
            f"flameshot full -p {path.join(HOME_DIR,'Pictures')}"), desc='capture all displays'),
    Key([MOD_KEY], "Print", lazy.spawn(
        "flameshot screen -p {path.join(HOME_DIR,'Pictures')}"), desc='capture current screen'),
]


SCREEN_BRIGHTNESS_BINDINGS: List[Key] = [
    Key([], "XF86MonBrightnessUp", lazy.spawn(
            "brightnessctl s 10%+"), desc='brightness up'),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
            "brightnessctl s 10%-"), desc='brightness down'),
]


AUDIO_LEVEL_BINDINGS: List[Key] = [
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume 0 +5%"), desc='volume up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute toggle"), desc='mute audio'),
    Key([], "XF86AudioMicMute", lazy.spawn(
            "pactl set-source-mute toggle"), desc='mute mic'),
]


MEDIA_PLAYER_BINDINGS: List[Key] = [
    Key([], "XF86AudioPlay", lazy.spawn(
            "playerctl play"), desc='play media'),
    Key([], "XF86AudioPause", lazy.spawn(
            "playerctl pause"), desc='pause media'),
    Key([], "XF86AudioStop", lazy.spawn(
            "playerctl stop"), desc='stop media play'),
    Key([], "XF86AudioPrev", lazy.spawn(
            "playerctl previous"), desc='play next media'),
    Key([], "XF86AudioNext", lazy.spawn(
            "playerctl next"), desc='play previous media'),
]
