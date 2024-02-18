#!/usr/bin/python3

from pyrob.api import *

def down_up(n):
    for _ in range(n):
        move_down()
        fill_cell()
    move_up(n-1)
    move_right()

@task(delay=0.01)
def task_4_11():
    move_right()
    for i in range(13,1,-1):
        down_up(i)
    move_down()
    fill_cell()
    move_down()
    while not wall_is_on_the_left():
        move_left()
    move_right()

if __name__ == '__main__':
    run_tasks()
