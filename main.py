import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from EightDigitSolverUI.mainwindow import *
from EightDigitSolver import dfs, bfs, astar, idastar


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.solve_btn.clicked.connect(self.on_solve)
        self.clear_btn.clicked.connect(self.on_clear)
        self.init_btn.clicked.connect(self.on_shuffle)
        self.init_state = None
        self.on_shuffle()

    def init_with(self):
        self.l_1_1.setText(str(self.init_state[0]))
        self.l_1_2.setText(str(self.init_state[1]))
        self.l_1_3.setText(str(self.init_state[2]))
        self.l_2_1.setText(str(self.init_state[3]))
        self.l_2_2.setText(str(self.init_state[4]))
        self.l_2_3.setText(str(self.init_state[5]))
        self.l_3_1.setText(str(self.init_state[6]))
        self.l_3_2.setText(str(self.init_state[7]))
        self.l_3_3.setText(str(self.init_state[8]))

    def on_solve(self):
        current_text = self.method.currentText()
        depth = self.depth.value()

        if current_text == "BFS":
            self.process.append("使用BFS算法求解中...")
            solver = bfs.BFS_Solver(self.init_state, depth)
        elif current_text == "DFS":
            self.process.append("使用DFS算法求解中...")
            solver = dfs.DFS_Solver(self.init_state, depth)
        elif current_text == "A*":
            self.process.append("使用A*算法求解中...")
            solver = astar.ASTAR_Solver(self.init_state, depth)
        else:
            self.process.append("使用IDA*算法求解中...")
            solver = idastar.IDASTAR_Solver(self.init_state, depth)

        solver.solve()
        self.process.append(str(solver.get_process()))

    def on_clear(self):
        self.process.setText("求解器就绪...")

    def on_shuffle(self):
        self.init_state = [0, 2, 3, 1, 4, 5, 7, 8, 6]
        random.shuffle(self.init_state)

        self.init_with()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
