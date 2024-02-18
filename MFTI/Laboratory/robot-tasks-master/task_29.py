#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_7():
    count_filled = 0
    while count_filled < 3:
        move_right()
        if cell_is_filled():
            count_filled += 1
        elif count_filled > 0:
            count_filled = 0
        if wall_is_on_the_right():
            count_filled = 3


if __name__ == '__main__':
    run_tasks()
