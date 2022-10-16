from libqtile.config import Group
import re
from subprocess import Popen, PIPE, STDOUT

GROUPS = [
    Group("0", label="⬤") if i == 10 else Group(f"{i}")
    for i in range(1, 11)
]


def decode_monitor_info(line: str):
    parts = re.split('\W+', line.strip())
    return parts[7], int(parts[2]), int(parts[3].split('x', 1)[-1])


def get_monitors():
    cmd = 'xrandr --listmonitors |  grep "^[ 0-9]"'
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    return [decode_monitor_info(line.decode("utf-8")) for line in ps.communicate()[0].splitlines()]
    