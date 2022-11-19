#!/usr/bin/python
from subprocess import run, Popen, PIPE

"""
You must change these device constants to adapt this script to your machine.
Find them by typing `xinput` in the terminal.
"""
KB_DEVICE = "AT Translated Set 2 keyboard"
TP_DEVICE = "DELL0B24:00 27C6:0D42 Touchpad"


def toggle_device(device):
    l1 = ["xinput", "list-props", device]
    l2 = ["grep", "Device Enabled"]

    p1 = Popen(l1, stdout=PIPE)
    p2 = run(l2, stdin=p1.stdout, capture_output=True)
    status = p2.stdout.decode().strip().split("\t")[1]

    if int(status) == 1:
        action = "disable"
    else:
        action = "enable"

    run(["xinput", action, device])


if __name__ == "__main__":
    toggle_device(KB_DEVICE)
    toggle_device(TP_DEVICE)
