from abc import abstractmethod
from unittest import result
import numpy as np


class SolverNET:
    def __init__(self, NumOfObs: int, NumOfUn: int):
        self.A: np.ndarray = np.zeros((NumOfObs, NumOfUn))
        self.l: np.ndarray = np.zeros((NumOfObs, 1))
        self.W: np.ndarray = np.zeros((NumOfObs, NumOfObs))
        self.dx: np.ndarray = np.zeros((NumOfUn, 1))

    @abstractmethod
    def Solve(self): raise NotImplementedError

    def __str__(self) -> str:
        return "Jacobian\n"+str(self.A)+"\nWeight:\n"+str(self.W)+"\nReduced Observation Vector:\n"+str(self.l)+"\n"+"Estimated Parameters:\n"+str(self.dx)+"\n"
