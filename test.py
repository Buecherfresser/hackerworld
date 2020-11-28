import numpy as np


def maze_runner(maze, directions):
    maze = np.array(maze)
    return print(np.where(maze == 2))


maze_runner([[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,2,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,0,1,0,1]],2)
