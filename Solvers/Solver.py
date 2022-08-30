#! Copyright (c) - 2022 Abdülkadir Çakır
from abc import abstractmethod
from unittest import result
import numpy as np


class SolverNET:
    def __init__(self, NumOfObs: int, NumOfUn: int):
        #Jacobian Matrix
        self.A: np.ndarray = np.zeros((NumOfObs, NumOfUn))
        #Reduced Observervations Vector
        self.l: np.ndarray = np.zeros((NumOfObs, 1))
        # Weight Matrix
        self.W: np.ndarray = np.zeros((NumOfObs, NumOfObs))
        # Estimates Vector
        self.dx: np.ndarray = np.zeros((NumOfUn, 1))
        # Root Mean Square Error
        self.m0 : float = 0.0
        # Normalized Equation Coefficent Matrix
        self.N : np.ndarray = None
        # Constants
        self.b :np.ndarray = None
        # Adjusted Observations
        self.L:np.ndarray = None
        # Inverse Weight Matrix of Unknown Parameters
        self.Qxx:np.ndarray = None
        # Mean Errors of Unknown Parameters
        self.mxx:np.ndarray = None
        # Inverse Weight Matrix of Observations
        self.Qll:np.ndarray = None
        # Inverse Weight Matrix of Adjusted Observations
        self.QLL:np.ndarray = None        
        # Residuals
        self.v:np.ndarray = None
        # Mean Error of Observations
        self.ml:np.ndarray = None
        # Mean Error of Adjusted Observations
        self.mL:np.ndarray = None
        # Mean Error of Residuals
        self.mv: np.ndarray=None
        # Covariance matrix of residuals
        self.Qvv: np.ndarray=None

    @abstractmethod
    def Solve(self): raise NotImplementedError
    
    @abstractmethod
    def ComputeStatistics(self):raise NotImplementedError

    def __str__(self) -> str:
        return "Jacobian\n"+str(self.A)+"\nWeight:\n"+str(self.W)+"\nReduced Observation Vector:\n"+str(self.l)+"\n"+"Estimated Parameters:\n"+str(self.dx)+"\n"
