#!/usr/bin/python3
"""
Məqsəd: Bütün qutuların açılıb-açılmadığını təyin edən metod
"""


def canUnlockAll(boxes):
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