from math import sqrt
import numpy


class PointNET:
    def __assign(self):
        #   Coordinates
        self.X: float = 0.0
        self.Y: float = 0.0
        self.Z: float = 0.0
        #   Weights
        self.Wx: float = 1.0
        self.Wy: float = 1.0
        self.Wz: float = 1.0
        #   Std. Errors
        self.Mx: float = 0.0
        self.My: float = 0.0
        self.Mz: float = 0.0

    @classmethod
    def FromCoordinates(self, name: str, x: float, y: float, z: float):
        res = PointNET(name)
        self.__assign(res)
        #   Coordinates
        res.X = x
        res.Y = y
        res.Z = z
        return res

    def __init__(self, Name: str):
        self.IsFixed = False
        self.name = Name
        self.__assign()

    # Distance to point in 3D
    def Dist2Point3D(self, Point) -> float:
        return sqrt((self.X - Point.X)**2 + (self.Y-Point.Y)**2 + (self.Z-Point.Z)**2)
    # Distance to point in 2D

    def Dist2Point2D(self, Point) -> float:
        return sqrt((self.X - Point.X)**2 + (self.Y-Point.Y)**2)

    # Computes vector to point
    def VectorTo(self, Point) -> numpy.ndarray:
        return numpy.asarray([self.X - Point.X, self.Y - Point.Y, self.Z - Point.Z])

    # ToString
    def __str__(self) -> str:
        result = "[Name:{} \tX: {:.3f} \tY: {:.3f} \tZ: {:.3f} ]"
        return result.format(self.name, self.X, self.Y, self.Z)
