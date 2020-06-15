import time
from EightDigitSolver import solver


class DFS_Solver(solver.Solver):
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
            if i[1] == node[1] and i[2] == node[2]:
                return True
        return False

    def write_path(self):
        end_state = self.open[-1]
        self.process += "共%d步:\n" % end_state[2]
        path = [end_state]
        while end_state[0]:
            end_state = end_state[0]
            path.append(end_state)
        path.reverse()

        for j in path:
            for i in range(3):
                self.process += str(j[1][i * 3:i * 3 + 3]) + "\n"

            self.process += "->\n"

    def dfs(self):
        while len(self.open):
            extand_state = self.open[-1]
            if extand_state[1] == self.target_state:
                self.open.append(extand_state)
                return True

            space_index = extand_state[1].index(0)
            extanded = False
            if extand_state[2] >= self.depth:
                state = self.open.pop()
                self.close.append(state)
            else:
                for i in range(len(self.di)):
                    if ((i == 0 and (space_index + self.di[i]) >= 0) or
                            (i == 1 and (space_index + self.di[i]) <= 8) or
                            (i == 2 and (space_index % 3 != 0)) or
                            (i == 3 and ((space_index + 1) % 3) != 0)):
                        state = extand_state[1].copy()
                        temp = state[space_index + self.di[i]]
                        state[space_index + self.di[i]] = 0
                        state[space_index] = temp
                        node_state = [extand_state, state, extand_state[2] + 1]
                        if state == self.target_state:
                            self.open.append(node_state)
                            return True
                        elif (not self.is_in_table(node_state, self.close)) and (not self.is_in_table(node_state,
                                                                                                      self.open)):
                            self.open.append(node_state)
                            extanded = True

                if not extanded:
                    self.open.pop()
                else:
                    self.close.append(extand_state)
                    self.open.remove(extand_state)

        return False
