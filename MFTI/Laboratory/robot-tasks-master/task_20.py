#!/usr/bin/python3

from pyrob.api import *


def right():
    for _ in range(26):
        move_right()
        fill_cell()
    move_down()

def left():
    for _ in range(26):
        move_left()
        fill_cell()
    move_down()

@task(delay=0.01)
def task_4_3():
    move_right()
    fill_cell()
    for _ in range(5):
        right()
        fill_cell()
        left()
        fill_cell()
    right()
    fill_cell()
    left()


if __name__ == '__main__':
    run_tasks()
