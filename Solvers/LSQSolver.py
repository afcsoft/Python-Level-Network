import imp
import numpy as np

from Solvers.Solver import SolverNET


class LSQSolverNET(SolverNET):
    def __init__(self, NumOfObs: int, NumOfUn: int):
        super().__init__(NumOfObs, NumOfUn)

    def Solve(self):
        self.dx = np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(
            self.A), self.W), self.A)), np.dot(np.dot(self.A.transpose(), self.W), self.l))

    def __str__(self) -> str:
        return super().__str__()
