#!/usr/bin/python3

from pyrob.api import *

def wall_right():
    if wall_is_on_the_right():
        while wall_is_above():
            move_left()
@task(delay=0.01)
def task_8_28():
    wall_right()
    while wall_is_above():
        move_right()
        wall_right()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
