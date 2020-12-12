class P:
    def __init__(self, id, arrive, exec_time, deadline):
        self.id = id
        self.arrive = arrive
        self.exec_time = exec_time
        self.deadline = deadline

procs = []
procs.append(P("P0", 0, 30, 100))
procs.append(P("P1", 20, 30, 230))
procs.append(P("P2", 55, 40, 145))
procs.append(P("P3", 85, 20, 135))
