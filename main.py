#TODO
#!RANSAC
#!Triangulation Network
#!Trilateration Network
#!GPS Network
from CommonNet.Observation import ObservationNET
from CommonNet.Point import PointNET
from CommonNet.Baseline import BaselineNET
from CommonNet.Network import NetworkNET
from LevelNet.Level import LevelNET

level=LevelNET(False,"Sample_Net",True)

P1=PointNET.FromCoordinates("P1",243214.0,0.0,0.0)
P2=PointNET.FromCoordinates("P2",0.0,0.0,0.0)
P3=PointNET.FromCoordinates("P3",0.0,0.0,0.0)
A=PointNET.FromCoordinates("A",0,0,80.673)
A.IsFixed=True

level.Points.append(A)
level.Points.append(P1)
level.Points.append(P2)
level.Points.append(P3)

level.Observations.append(ObservationNET(A,P1,tuple([43.156]),tuple([0.65])))
level.Observations.append(ObservationNET(P2,P1,tuple([19.218]),tuple([0.80])))
level.Observations.append(ObservationNET(P2,P3,tuple([33.524]),tuple([1.00])))
level.Observations.append(ObservationNET(A,P3,tuple([57.440]),tuple([1.40])))
level.Observations.append(ObservationNET(A,P2,tuple([23.962]),tuple([1.50])))
level.Observations.append(ObservationNET(P1,P3,tuple([14.267]),tuple([1.95])))

level.Points = level.Solve()


for i in level.Points:
    print(i)