#!/usr/bin/python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked."""
    if not boxes:
        return False
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])
    return all(unlocked)
