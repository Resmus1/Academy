#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_7():
    flag = True
    while flag:
        if wall_is_above():
            move_right()
        elif wall_is_beneath():
            move_right()
        else:
            flag = False


if __name__ == '__main__':
    run_tasks()
