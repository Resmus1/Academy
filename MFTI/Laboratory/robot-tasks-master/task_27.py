#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_7_5():
    move_right()
    fill_cell()
    count_fill = steps = 0
    while not wall_is_on_the_right():
        if count_fill < steps:
            count_fill += 1
            move_right()
        else:
            count_fill = 0
            steps += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()


if __name__ == '__main__':
    run_tasks()
