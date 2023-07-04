#!/usr/bin/python3
"""This is program determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked"""
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    keys_stack = [0]

    while keys_stack:
        curr_box = keys_stack.pop()
        keys = boxes[curr_box]

        for key in keys:
            if key >= 0 and key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)
