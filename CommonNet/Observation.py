import imp
from unittest import result


#! Copyright (c) - 2022 Abdülkadir Çakır
from CommonNet.Point import PointNET


class ObservationNET:
    def __init__(self, From: PointNET, To: PointNET, Value: tuple, Weight: tuple):
        self.From: PointNET = From
        self.To: PointNET = To
        self.Value = Value
        self.Weight = Weight
        self.isDiscarded: bool = False
    def __str__(self):
        result="[Observation: From:{}\t To:{}\t Value:{}\t Weight:{}]"
        return result.format(self.From.name,self.To.name,str(self.Value),str(self.Weight))