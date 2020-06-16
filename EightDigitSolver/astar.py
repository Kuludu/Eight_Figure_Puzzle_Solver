import time
import heapq as hq
from EightDigitSolver import solver


class Node:
    def __init__(self, pre, state, depth):
        self.pre = pre
        self.state = state
        self.depth = depth
        self.diff = self.cal_diff()

    def __lt__(self, other):
        if self.diff + self.depth < other.diff + other.depth:
            return True
        else:
            return False

    def cal_diff(self):
        ret = 0
        for index, value in enumerate(self.state):
            if value != index + 1:
                ret += 1

        return ret


class ASTAR_Solver(solver.Solver):
    def __init__(self, init_state, depth):
        super().__init__(init_state, depth)
        self.open = [Node(None, init_state, 0)]
        self.close = [Node(None, init_state, 0)]
        hq.heapify(self.open)

    def solve(self):
        start = time.time()

        flag = self.dfs()
        if not flag:
            self.process = "算法未找到解"
        else:
            self.write_path()

        end = time.time()
        self.solve_time = end - start

    def is_in_table(self, node, table):
        for i in table:
            if i.state == node.state and i.depth == node.depth:
                return True
        return False

    def write_path(self):
        end_state = self.open[0]
        self.process += "共%d步:\n" % end_state.depth
        path = [end_state]
        while end_state.pre:
            end_state = end_state.pre
            path.append(end_state)
        path.reverse()

        for j in path:
            for i in range(3):
                self.process += str(j.state[i * 3:i * 3 + 3]) + "\n"

            self.process += "->\n"

    def dfs(self):
        while len(self.open):
            extand_state = self.open[0]
            if extand_state.state == self.target_state:
                hq.heappush(self.open, extand_state)
                return True

            space_index = extand_state.state.index(0)
            extanded = False
            if extand_state.depth > self.depth:
                state = hq.heappop(self.open)
                self.close.append(state)
            else:
                for i in range(len(self.di)):
                    if ((i == 0 and (space_index + self.di[i]) >= 0) or
                            (i == 1 and (space_index + self.di[i]) <= 8) or
                            (i == 2 and (space_index % 3 != 0)) or
                            (i == 3 and ((space_index + 1) % 3) != 0)):
                        state = extand_state.state.copy()
                        temp = state[space_index + self.di[i]]
                        state[space_index + self.di[i]] = 0
                        state[space_index] = temp
                        next_state = Node(extand_state, state, extand_state.depth + 1)
                        if (not self.is_in_table(next_state, self.close)) and (not self.is_in_table(next_state,
                                                                                                    self.open)):
                            hq.heappush(self.open, next_state)
                            extanded = True

                if not extanded:
                    self.open.pop()
                else:
                    self.close.append(extand_state)
                    self.open.remove(extand_state)

        return False
