#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_6():
    count_filled = 0
    while count_filled < 5:
        move_right()
        if cell_is_filled():
            count_filled += 1


if __name__ == '__main__':
    run_tasks()
