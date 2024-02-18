#!/usr/bin/python3

from pyrob.api import *


def right():
    move_right()
    while not wall_is_on_the_right():
        move_right()
def left():
    move_left()
    while not wall_is_on_the_left():
        move_left()
@task(delay=0.1)
def task_8_22():
    flag = True
    while flag:
        if wall_is_on_the_right() and wall_is_on_the_left():
            move_up()
        elif wall_is_above() and wall_is_on_the_left():
            right()
            flag = False
        elif wall_is_above() and wall_is_on_the_right():
            left()
            flag = False



if __name__ == '__main__':
    run_tasks()
