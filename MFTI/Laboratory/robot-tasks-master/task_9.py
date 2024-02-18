#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    flag = True
    while flag:
        if not wall_is_above():
            fill_cell()
        if not wall_is_on_the_right():
            move_right()
        else:
            flag = False

if __name__ == '__main__':
    run_tasks()
