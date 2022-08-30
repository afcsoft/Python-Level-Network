#! Copyright (c) - 2022 Abdülkadir Çakır
from re import A
from CommonNet import Point
from CommonNet.Point import PointNET
from CommonNet.Network import NetworkNET
from CommonNet.Observation import ObservationNET
from typing import List
from Solvers.LSQSolver import LSQSolverNET
import numpy as np


class LevelNET(NetworkNET):

    def __init__(self, Is2D: bool, name: str, UseDistanceAsWeight: bool):
        super().__init__(Is2D, name, "Level Network", 1)
        self.UseDist: bool = UseDistanceAsWeight
        self.SLS: LSQSolverNET = None
        self.ValidObservations: List[ObservationNET] = None

    # Compute Weights from distance or fill diagonal with ones
    def ComputeWeights(self):
        if self.UseDist == False:
            np.fill_diagonal(self.SLS.W, 1)
        else:
            for i in range(len(self.ValidObservations)):
                self.SLS.W[i, i] = 1 / self.ValidObservations[i].Weight[0]

    # Check any zero elevations for ComputeHeights
    def NeedToFill(self) -> bool:
        for i in self.ValidObservations:
            if (i.From.Z == 0) or (i.To.Z == 0):
                return True

    # Compute Apriori Heights,if not assigned
    def ComputeHeights(self):
        while (self.NeedToFill()):
            for i in self.ValidObservations:
                if i.From.Z == 0:
                    if i.To.Z != 0:
                        i.From.Z = i.To.Z-i.Value[0]
                if i.To.Z == 0:
                    if i.From.Z != 0:
                        i.To.Z = i.From.Z + i.Value[0]

    # Compute Jacobian Matrix
    # f(HTo-Hfrom) = dZ
    def ComputeJacobian(self):
        for i in range(len(self.ValidObservations)):
            obs = self.ValidObservations[i]
            for j in range(len(self.Points)):
                point = self.Points[j]
                if (obs.From == point):
                    self.SLS.A[i, j] = 0 if point.IsFixed else -1
                if (obs.To == point):
                    self.SLS.A[i, j] = 0 if point.IsFixed else 1
        # Eliminate empty column(s) caused by fixed points
        idx = np.argwhere(np.all(self.SLS.A[..., :] == 0, axis=0))
        self.SLS.A = np.delete(self.SLS.A, idx, axis=1)

    # Compute Reduced Observation Vector
    #  l = Observed - Computed
    def ComputeReducedObservations(self):
        for i in range(len(self.ValidObservations)):
            obs = self.ValidObservations[i]
            self.SLS.l[i, 0] = obs.Value[0] - (obs.To.Z - obs.From.Z)

    # Solve Least Squares and add estimated deltas to original elevations
    def Solve(self) -> List[PointNET]:
        if not self.IsSolvable():
            return False

        self.ValidObservations = self.GetValidObservations()
        for i in range(0, 3):
            self.ComputeHeights()
            self.SLS = LSQSolverNET(len(self.ValidObservations), len(self.Points))

            self.ComputeWeights()
            self.ComputeJacobian()
            self.ComputeReducedObservations()
            self.SLS.Solve()
            self.SLS.ComputeStatistics()
            index = 0
            for i in range(len(self.Points)):
                point = self.Points[i]
                if (point.IsFixed):
                    continue
                point.Z+self.SLS.dx[index, 0]
                index += 1

        return self.Points
