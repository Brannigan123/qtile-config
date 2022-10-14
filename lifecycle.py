import os
import subprocess

from layouts.layout_factory import FLOATING_TYPES


def clean_up():
    os.popen('find ~/.config/qtile/. | grep -E "__pycache__$" | xargs rm -rf')


def startup_daemons():
    path = '~/.config/daemon_scripts/startup_daemons.sh'
    subprocess.call(['sh', os.path.expanduser(path)])


def set_floating_windows(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in FLOATING_TYPES):
        window.floating = True
