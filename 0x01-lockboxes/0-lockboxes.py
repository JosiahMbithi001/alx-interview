#!/usr/bin/env python3
"""This File Contains a function canUnlock All"""


def canUnlockAll(boxes):
    """This Function unlocks the Box in an index"""

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    for i in range(num_boxes):
        if not unlocked_boxes[i]:
            continue

        box_keys = boxes[i]
        for key in box_keys:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True

    return all(unlocked_boxes)
