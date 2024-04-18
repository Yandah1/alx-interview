#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
'''


def canUnlockAll(boxes):
    '''Check if all boxes can open sucessfully or not'''
    num_boxes = len(boxes)
    keys = set(boxes[0])
    opened_boxes = [0]

    for box in opened_boxes:
        for key in boxes[box]:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                opened_boxes.append(key)
                keys.update(boxes[key])

    for i in range(1, num_boxes):
        if i not in opened_boxes:
            return False
    return True
