#!/usr/bin/python3

from pyrob.api import *

def move():
    while not wall_is_on_the_right():
        move_right()
        while not wall_is_beneath():
            move_down()
            flag = True


@task(delay=0.01)
def task_8_30():
    flag = True
    while flag:
        flag = False
        move()
        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                move_down()
                flag = True




if __name__ == '__main__':
    run_tasks()
