import imp


from CommonNet.Point import PointNET


class ObservationNET:
    def __init__(self, From: PointNET, To: PointNET, Value: tuple, Weight: tuple):
        self.From: PointNET = From
        self.To: PointNET = To
        self.Value = Value
        self.Weight = Weight
        self.isDiscarded: bool = False
