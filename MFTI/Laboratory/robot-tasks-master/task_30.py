#!/usr/bin/python3

from pyrob.api import *

def circle(distance, x):
    for _ in range(distance - x):
        move_down()
        fill_cell()
    move_down()
    for _ in range(distance - x):
        move_left()
        fill_cell()
    move_left()
    for _ in range(distance - x):
        move_up()
        fill_cell()
    move_up()
    for _ in range(distance - x):
        move_right()
        fill_cell()
    move_down()

def length():
    count_lenght = 1
    while not wall_is_on_the_right():
        move_right()
        count_lenght += 1
    return count_lenght

def triangels(distance, turn, step=2):
    for _ in range(turn):
        circle(distance, step)
        step += 2

def end():
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()

@task(delay=0.01)
def task_9_3():
    long = length()
    turn = long // 2
    triangels(long, turn)
    end()

if __name__ == '__main__':
    run_tasks()
