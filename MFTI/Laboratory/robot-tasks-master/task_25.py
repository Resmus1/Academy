#!/usr/bin/python3

from pyrob.api import *


def cross():
    for _ in range(2):
        fill_cell()
        move_right()
        fill_cell()
    move_down()
    move_left()
    for _ in range(2):
        fill_cell()
        move_up()
        fill_cell()


@task(delay=0.01)
def task_2_2():
    move_down(2)
    for _ in range(4):
        cross()
        move_right(3)
        move_down(1)
    cross()
    move_left()


if __name__ == '__main__':
    run_tasks()
