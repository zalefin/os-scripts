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


def show_seek_path(path_list, name, total):
    path_list = [PREVIOUS] + path_list
    if not SHOW_PLOTS:
        return
    # disk path:
    y = np.array(list(reversed(list(range(len(path_list))))))
    x = np.array(list(reversed(path_list)))
    linvals = [[np.linspace(y[i], y[i + 1], 1000), np.linspace(x[i], x[i + 1], 1000)] for i in range(len(y) - 1)]

    # pending disk movement:
    for xs, ys in linvals[:-1]:
        plt.plot(xs + (abs(xs[0] - xs[-1]) / 2), ys, label="(" + str(abs(int(ys[0] - ys[-1]))) + ")", color="black", alpha=0.5)

    # previous disk movement:
    for xs, ys in [linvals[-1]]:
        plt.plot(xs + (abs(xs[0] - xs[-1]) / 2), ys, label="(" + str(int(abs(ys[0] - ys[-1]))) + ")", color="blue", alpha=0.5)

    labelLines(plt.gca().get_lines(), xvals=y, zorder=2.5, align=False, drop_label=False, color='black')

    plt.title(str(QUEUE) + "\n\n$" + name + "_{total} = " + str(total) + "$\n\n" + str(path_list[1:]).replace(", ", " -> "))

    for index, path in enumerate(path_list[2:]):
        t = plt.text(index + 2.3, path - 0.3, str(path))
        t.set_bbox(dict(facecolor='grey', alpha=0.5, edgecolor='black'))

    for index, path in enumerate([path_list[0]]):
        t = plt.text(index + 0.3, path - 0.3, str(path))
        t.set_bbox(dict(facecolor='blue', alpha=0.3, edgecolor='blue'))

    for index, path in enumerate([path_list[1]]):
        t = plt.text(index + 1.3, path - 0.3, str(path))
        t.set_bbox(dict(facecolor='green', alpha=0.3, edgecolor='green'))

    plt.axhline(y=0)
    plt.axhline(y=MAX_CYLNDER)
    plt.show()


def FCFS():
    path = [CURRENT] + QUEUE
    total = 0
    for i in range(len(path) - 1):
        total += abs(path[i] - path[i + 1])

    print("FCFS:", total)
    show_seek_path(path, "FCFS", total)


def SCAN():
    if PREVIOUS < CURRENT:
        direction = "up"
    elif PREVIOUS > CURRENT:
        direction = "down"

    above = [pos for pos in QUEUE if pos > CURRENT]
    below = [pos for pos in QUEUE if pos < CURRENT]

    if direction == "up":
        if MAX_CYLNDER not in above:
            above.append(MAX_CYLNDER)

    elif direction == "down":
        if 0 not in below:
            below.append(0)

    if direction == "up":
        ordered = sorted(above) + list(reversed(sorted(below)))

    if direction == "down":
        ordered = list(reversed(sorted(below))) + sorted(above)

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("SCAN:", total)
    show_seek_path(ordered, "SCAN", total)


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
    show_seek_path(plot_list, "SSTF", total)


def CSCAN():
    if PREVIOUS < CURRENT:
        direction = "up"
    elif PREVIOUS > CURRENT:
        direction = "down"

    above = [pos for pos in QUEUE if pos > CURRENT]
    below = [pos for pos in QUEUE if pos < CURRENT]

    # Only add upper and lower bound if the arm actually needs to "reset"
    if (len(below) != 0 and direction == "up"):
        if MAX_CYLNDER not in above:
            above.append(MAX_CYLNDER)
        if 0 not in below:
            below.append(0)

    # If arm is already "resetting" it must go all the way to 0
    elif direction == "down":
        if 0 not in below:
            below.append(0)

    # If going up, arm goes until MAX_CYLNDER then resets to do all values below where it started
    if direction == "up":
        ordered = sorted(above) + list(sorted(below))

    # If going down, arm is "resetting" all the way to 0
    if direction == "down":
        ordered = list(sorted(below)) + list(sorted(above))

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("C-SCAN:", total)
    show_seek_path(ordered, "C-SCAN", total)


def CLOOK():
    if PREVIOUS < CURRENT:
        direction = "up"
    elif PREVIOUS > CURRENT:
        direction = "down"

    above = [pos for pos in QUEUE if pos > CURRENT]
    below = [pos for pos in QUEUE if pos < CURRENT]

    # if going up finish the rest above, then go to lowest remaining and start working up again
    if direction == "up":
        ordered = sorted(above) + sorted(below)

    # If going down, then arm is "resetting" all the way to the lowest value
    if direction == "down":
        ordered = sorted(below) + sorted(above)

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("C-LOOK:", total)
    show_seek_path(ordered, "C-LOOK", total)


def LOOK():
    if PREVIOUS < CURRENT:
        direction = "up"
    elif PREVIOUS > CURRENT:
        direction = "down"

    above = [pos for pos in QUEUE if pos > CURRENT]
    below = [pos for pos in QUEUE if pos < CURRENT]

    if direction == "up":
        ordered = sorted(above) + list(reversed(sorted(below)))

    if direction == "down":
        ordered = list(reversed(sorted(below))) + sorted(above)

    ordered = [CURRENT] + ordered
    total = 0
    for i in range(len(ordered) - 1):
        total += abs(ordered[i] - ordered[i + 1])

    print("LOOK:", total)
    show_seek_path(ordered, "LOOK", total)


if __name__ == "__main__":
    disk_schedulers = (FCFS, SSTF, SCAN, LOOK, CSCAN, CLOOK)
    for sched in disk_schedulers:
        sched()
