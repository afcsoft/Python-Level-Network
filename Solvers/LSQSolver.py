#! Copyright (c) - 2022 Abdülkadir Çakır
from math import sqrt
import numpy as np
from Solvers.Solver import SolverNET


class LSQSolverNET(SolverNET):
    def __init__(self, NumOfObs: int, NumOfUn: int):
        super().__init__(NumOfObs, NumOfUn)
        self.n=NumOfObs
        self.u=NumOfUn

    def Solve(self):
        self.dx = np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(
            self.A), self.W), self.A)), np.dot(np.dot(self.A.transpose(), self.W), self.l))
    def ComputeStatistics(self):
        #Residuals
        self.v = np.dot(self.A,self.dx)-self.l
        # RMS
        self.m0 = np.sqrt((np.dot(np.dot(np.transpose(self.v),self.W),self.v))/(self.n-self.u))[0,0]
        # Inverse Weight Matrix of Unknown Parameters
        self.Qxx = np.linalg.inv(np.dot(np.dot(np.transpose(self.A) , self.W ), self.A))
        self.mxx = self.m0*np.sqrt(np.diag(np.abs(self.Qxx)))
        self.Qll = self.m0 / np.sqrt(self.W)
        self.QLL = np.dot(np.dot(self.A , self.Qxx), np.transpose(self.A))
        self.mL = self.m0 * np.sqrt(np.diag(np.abs(self.QLL)))
        self.Qvv = self.QLL - self.Qll
        self.mv = self.m0 * np.sqrt(np.diag(np.abs(self.Qvv)))
        self.ml = self.m0 * np.sqrt(np.diag(np.abs(self.Qll)))
        self.L = self.l + self.v


    def __str__(self) -> str:
        return super().__str__()
