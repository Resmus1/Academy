#!/usr/bin/python3

from pyrob.api import *


def cross():
    for _ in range(3):
        move_down()
        fill_cell()
    move_up()
    move_left(2)
    for _ in range(3):
        move_right()
        fill_cell()


@task
def task_2_1():
    move_right(2)
    cross()
    move_up()
    move_left(2)


if __name__ == '__main__':
    run_tasks()
