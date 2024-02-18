#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    count = 0
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        count += 1
        move_right()
    move_down()
    for _ in range(count):
        move_left()


if __name__ == '__main__':
    run_tasks()
