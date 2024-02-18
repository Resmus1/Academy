#!/usr/bin/python3

from pyrob.api import *
def down():
    while not wall_is_beneath():
        move_down()
        fill_cell()


def up ():
    while not wall_is_above():
        move_up()
        fill_cell()


def right():
    if not wall_is_on_the_right():
        move_right()
        fill_cell()


def left():
    while not wall_is_on_the_left():
        move_left()

@task(delay=0.01)
def task_5_10():
    flag = True
    fill_cell()
    while flag:
        down()
        right()
        up()
        right()
        down()
        if wall_is_beneath() and wall_is_on_the_right():
            flag = False
    left()


if __name__ == '__main__':
    run_tasks()
