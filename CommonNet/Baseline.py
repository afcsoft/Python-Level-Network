import numpy
from CommonNet.Point import PointNET


class BaselineNET:
    def __init__(self) -> None:
        self.Start = PointNET.FromCoordinates(0, 0, 0)
        self.End = PointNET.FromCoordinates(0, 0, 0)

        self.Wx = 1.0
        self.Wy = 1.0
        self.Wz = 1.0

    @classmethod
    def FromPoints(self, Start, End):
        res = BaselineNET()
        res.Start = Start
        res.End = End
        return res

    def Length(self) -> float:
        return self.Start.Dist2Point3D(self.End)

    def ToDelta(self) -> numpy.array:
        return self.End.VectorTo(self.Start)

    def __str__(self) -> str:
        return "Start: " + str(self.Start) + " End: " + str(self.End)
