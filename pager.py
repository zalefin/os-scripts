#!/usr/bin/env python3


PAGES = [3, 2, 4, 3, 4, 2, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 5, 6, 7, 2, 1]
PAGES = [1, 2, 3, 1, 4, 1, 2, 4, 2, 4, 3]
PAGES = [0, 1, 2, 3, 0, 1, 4, 0, 1, 2, 3, 4]
FRAME_ALLOC = 3


def fifo_page(req_pages, alloc):
    alloc_tail = 0
    frame_history = []
    frame = [None for _ in range(alloc)]
    page_faults = 0
    for i in range(len(req_pages)):
        if req_pages[i] not in frame:
            frame[alloc_tail] = req_pages[i]
            alloc_tail = (alloc_tail + 1) % alloc
            frame_history.append(frame.copy())
            page_faults += 1
        else:
            not_filled = frame.count(None)
            frame_history.append(
                ["-" for _ in range(alloc - not_filled)] + [" " for _ in range(not_filled)]
            )

    print("\nFIFO Page faults:", page_faults)
    for row in list(map(list, zip(*frame_history))):
        for thing in row:
            if thing is None:
                print(" , ", end="")
            else:
                print(str(thing) + r', ', end="")
        print()


def opt_page(req_pages, alloc):
    frame_history = []
    frame = [None for _ in range(alloc)]
    page_faults = 0
    for i in range(len(req_pages)):
        if req_pages[i] not in frame:
            if None in frame:
                frame[frame.index(None)] = req_pages[i]
                frame_history.append(frame.copy())
                page_faults += 1
            else:
                look_ahead = {}
                for page in frame:
                    try:
                        look_ahead[page] = req_pages.index(page, i)
                    except ValueError:
                        look_ahead[page] = float("inf")
                frame[frame.index(max(look_ahead, key=look_ahead.get))] = req_pages[i]
                frame_history.append(frame.copy())
                page_faults += 1
        else:
            not_filled = frame.count(None)
            frame_history.append(
                ["-" for _ in range(alloc - not_filled)] + [" " for _ in range(not_filled)]
            )

    print("\nOPT Page faults:", page_faults)
    for row in list(map(list, zip(*frame_history))):
        for thing in row:
            if thing is None:
                print(" , ", end="")
            else:
                print(str(thing) + r', ', end="")
        print()


def lru_page(req_pages, alloc):
    frame_history = []
    frame = [None for _ in range(alloc)]
    page_faults = 0
    for i in range(len(req_pages)):
        if req_pages[i] not in frame:
            if None in frame:
                frame[frame.index(None)] = req_pages[i]
                frame_history.append(frame.copy())
                page_faults += 1
            else:
                look_back = {}
                for page in frame:
                    look_back[page] = req_pages[i - 1::-1].index(page)
                frame[frame.index(max(look_back, key=look_back.get))] = req_pages[i]
                frame_history.append(frame.copy())
                page_faults += 1
        else:
            not_filled = frame.count(None)
            frame_history.append(
                ["-" for _ in range(alloc - not_filled)] + [" " for _ in range(not_filled)]
            )

    print("\nLRU Page faults:", page_faults)
    for row in list(map(list, zip(*frame_history))):
        for thing in row:
            if thing is None:
                print(" , ", end="")
            else:
                print(str(thing) + r', ', end="")
        print()


if __name__ == "__main__":
    fifo_page(PAGES, FRAME_ALLOC)
    opt_page(PAGES, FRAME_ALLOC)
    lru_page(PAGES, FRAME_ALLOC)
