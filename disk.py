#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from labellines import labelLine, labelLines

MAX_CYLNDER = 4999
QUEUE = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
CURRENT = 2150
PREVIOUS = 1805

SHOW_PLOTS = True


def show_seek_path(path_list, name):
    if not SHOW_PLOTS:
        return
    # disk path:
    y = np.array(list(reversed(list(range(len(path_list))))))
    x = np.array(path_list)
    linvals = [[np.linspace(y[i],y[i+1],1000),np.linspace(x[i], x[i+1], 1000)] for i in range(len(y)-1)]
    for xs, ys in linvals:
        plt.plot(xs+(abs(xs[0]-xs[-1])/2), ys, label=str(abs(ys[0]-ys[-1])))
    labelLines(plt.gca().get_lines(), xvals=y, zorder=2.5, align=False, drop_label=False)

    plt.title(str(QUEUE) + "\n" + name + "\n" + str(path_list))
    plt.axhline(y=0)
    plt.axhline(y=MAX_CYLNDER)
    plt.show()


def FCFS():
    path = [CURRENT] + QUEUE
    total = 0
    for i in range(len(path) - 1):
        total += abs(path[i] - path[i + 1])

    print("FCFS:", total)
    show_seek_path(path, "FCFS")


def SCAN():
    if PREVIOUS < CURRENT:
        direction = "right"
    elif PREVIOUS > CURRENT:
        direction = "left"

    right_side = [pos for pos in QUEUE if pos > CURRENT]
    left_side = [pos for pos in QUEUE if pos < CURRENT]

    if direction == "right":
        if MAX_CYLNDER not in right_side:
            right_side.append(MAX_CYLNDER)

    elif direction == "left":
        if 0 not in left_side:
            left_side.append(0)

    if direction == "right":
        ordered = sorted(right_side) + list(reversed(sorted(left_side)))

    if direction == "left":
        ordered = list(reversed(sorted(left_side))) + sorted(right_side)

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("SCAN:", total)
    show_seek_path(ordered, "SCAN")


def SSTF():
    remaining = QUEUE.copy()
    current_cylnder = CURRENT
    total = 0
    plot_list = [CURRENT]
    while len(remaining) > 0:
        next_cylnder = min(remaining, key=lambda x: abs(x - current_cylnder))
        plot_list.append(next_cylnder)
        total += abs(next_cylnder - current_cylnder)
        remaining.pop(remaining.index(next_cylnder))
        current_cylnder = next_cylnder

    print("SSTF:", total)
    show_seek_path(plot_list, "SSTF")


def CSCAN():
    if PREVIOUS < CURRENT:
        direction = "right"
    elif PREVIOUS > CURRENT:
        direction = "left"

    right_side = [pos for pos in QUEUE if pos > CURRENT]
    left_side = [pos for pos in QUEUE if pos < CURRENT]

    if MAX_CYLNDER not in right_side:
        right_side.append(MAX_CYLNDER)
    if 0 not in left_side:
        left_side.append(0)

    if direction == "right":
        ordered = sorted(right_side) + list(sorted(left_side))

    if direction == "left":
        ordered = list(reversed(sorted(left_side))) + list(reversed(sorted(right_side)))

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("C-SCAN:", total)
    show_seek_path(ordered, "C-SCAN")


def CLOOK():
    if PREVIOUS < CURRENT:
        direction = "right"
    elif PREVIOUS > CURRENT:
        direction = "left"

    right_side = [pos for pos in QUEUE if pos > CURRENT]
    left_side = [pos for pos in QUEUE if pos < CURRENT]

    if direction == "right":
        ordered = sorted(right_side) + list(sorted(left_side))

    if direction == "left":
        ordered = list(reversed(sorted(left_side))) + list(reversed(sorted(right_side)))

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("C-LOOK:", total)
    show_seek_path(ordered, "C-LOOK")


def LOOK():
    if PREVIOUS < CURRENT:
        direction = "right"
    elif PREVIOUS > CURRENT:
        direction = "left"

    right_side = [pos for pos in QUEUE if pos > CURRENT]
    left_side = [pos for pos in QUEUE if pos < CURRENT]

    if direction == "right":
        ordered = sorted(right_side) + list(reversed(sorted(left_side)))

    if direction == "left":
        ordered = list(reversed(sorted(left_side))) + sorted(right_side)

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("LOOK:", total)
    show_seek_path(ordered, "LOOK")


if __name__ == "__main__":
    disk_schedulers = (FCFS, SSTF, SCAN, LOOK, CSCAN, CLOOK)
    for sched in disk_schedulers:
        sched()
