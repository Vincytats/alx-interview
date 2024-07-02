#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    :param boxes: list of lists
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]
    
    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    
    return all(visited)
