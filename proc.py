#!/usr/bin/env python
class P:
    def __init__(self, id, arrive, exec_time, deadline):
        self.id = id
        self.arrive = arrive
        self.exec_time = exec_time
        self.deadline = deadline


class FCFS(object):
    def __init__(self, procs):
        # NO timeslice, does not use preemption
        self.procs = procs
        self.t = 0
        self.queue = []
        self.current = None

    def _all_done(self):
        for proc in self.procs:
            if proc.exec_time > 0:
                return False
        return True

    def tick(self):
        for proc in self.procs:
            if self.t == proc.arrive:
                self.queue.append(proc)

        if not self.current:
            if len(self.queue):
                self.current = self.queue.pop(0)
                print(self.current.id, self.t)

        if self.current:
            self.current.exec_time -= 1

            if self.current.exec_time <= 0:
                self.current = None
        self.t += 1

    def run(self):
        while not self._all_done():
            self.tick()
        # print finished time
        print("NONE", self.t)

class EDF(object):
    def __init__(self, procs, time_slice):
        self.procs = procs
        self.t = 0
        self.queue = []
        self.current = None
        self.slice_count = 0
        self.time_slice = time_slice

    def _all_done(self):
        for proc in self.procs:
            if proc.exec_time > 0:
                return False
        return True

    def tick(self):
        for proc in self.procs:
            if self.t == proc.arrive:
                self.queue.append(proc)

        if len(self.queue):
            self.queue = sorted(self.queue, key=lambda proc: proc.deadline)
            if not self.current:
                self.slice_count = 0
                self.current = self.queue[0]
                print(self.current.id, self.t)
            elif self.slice_count == self.time_slice or self.queue[0] != self.current:
                self.slice_count = 0
                self.current = self.queue[0]
                print(self.current.id, self.t)

        if self.current:
            self.current.exec_time -= 1
            self.slice_count += 1

            if self.current.exec_time <= 0:
                self.queue.remove(self.current)
                self.current = None
        self.t += 1

    def run(self):
        while not self._all_done():
            self.tick()
        # print finished time
        print("NONE", self.t)

procs = []
procs.append(P("P0", 0, 30, 100))
procs.append(P("P1", 20, 90, 230))
procs.append(P("P2", 55, 40, 145))
procs.append(P("P3", 85, 20, 135))

# fcfs = FCFS(procs)
# fcfs.run()
edf = EDF(procs, 20)
edf.run()

