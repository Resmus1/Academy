#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_21():
    flag = True
    while flag:
        if wall_is_above() and wall_is_on_the_left():
            for _ in range(9):
                move_right()
                move_down()
                flag = False
        elif wall_is_above() and wall_is_on_the_right():
            for _ in range(9):
                move_left()
                move_down()
                flag = False
        elif wall_is_beneath() and wall_is_on_the_right():
            for _ in range(9):
                move_left()
                move_up()
                flag = False
        elif wall_is_beneath() and wall_is_on_the_left():
            for _ in range(9):
                move_right()
                move_up()
                flag = False

if __name__ == '__main__':
    run_tasks()
