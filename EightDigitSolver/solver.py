class Solver:
    def __init__(self, init_state, depth):
        self.process = str()
        self.init_state = init_state
        self.target_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.depth = depth
        self.solve_time = 0
        self.open = [[None, init_state,  0]]
        self.close = [[None, init_state, 0]]
        self.di = [-3, 3, -1, 1]

    def solve(self):
        pass

    def get_process(self):
        self.process += "\n算法求解时间：%.2fs" % self.solve_time
        return self.process
