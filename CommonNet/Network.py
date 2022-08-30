from abc import abstractmethod
from unittest import result
from CommonNet.Point import PointNET
from CommonNet.Baseline import BaselineNET
from CommonNet.Observation import ObservationNET
from typing import List


class NetworkNET:
    def __init__(self, Is2D: bool, name: str, NetType: str, NumOfParameters: int):
        self.Points: List[PointNET] = []
        self.Observations: List[ObservationNET] = []

        self.Is2D: bool = Is2D
        self.name: str = name
        self.NetType: str = NetType
        self.NumOfParameters: int = NumOfParameters

    def DegreeOfFreedom(self) -> int:
        return len(self.GetValidObservations())-(len(self.Points) * self.NumOfParameters)

    def IsSolvable(self) -> int:
        return self.DegreeOfFreedom() > 0

    def __str__(self) -> str:
        result = "\t"+self.name + "(" + self.NetType + ")" + "\t\n"
        result += "Points:\n"
        for i in self.Points:
            result += str(i)+"\n"

        result += "Observations:\n"
        for i in self.Observations:
            result += str(i)+"\n"

        result += "3D:"
        result += "No" if self.Is2D else "Yes"
        return result

    @abstractmethod
    def Solve(self): raise NotImplementedError

    # Returns number of discarded observations
    def CheckObservations(self) -> int:
        # Check  for duplicates
        for i in range(len(self.Observations)):
            obs1 = self.Observations[i]
            for j in range(len(self.Observations)):
                if i == j:
                    continue
                obs2 = self.Observations[j]
                if ((obs1.From.name == obs2.From.name) or (obs1.To.name == obs2.To.name)):
                    obs2.isDiscarded = True

    def GetValidObservations(self) -> List[ObservationNET]:
        result = []
        for i in self.Observations:
            if (not i.isDiscarded):
                result.append(i)
        return result
