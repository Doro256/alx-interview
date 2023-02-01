#!/usr/bin/python3
""" Script that that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)
