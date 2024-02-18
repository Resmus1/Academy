#!/usr/bin/python3

from pyrob.api import *


def cross():
    move_right()
    for _ in range(2):
        fill_cell()
        move_down()
        fill_cell()
    move_left()
    move_up()
    for _ in range(2):
        fill_cell()
        move_right()
        fill_cell()


def line_cross():
    for _ in range(9):
        cross()
        move_up()
        move_right(2)
    cross()


def left():
    while not wall_is_on_the_left():
        move_left()
    move_down(3)


def last_left():
    while not wall_is_on_the_left():
        move_left()
    move_up()


@task(delay=0.01)
def task_2_4():
    for _ in range(4):
        line_cross()
        left()
    line_cross()
    last_left()


if __name__ == '__main__':
    run_tasks()
