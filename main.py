#! Copyright (c) - 2022 Abdülkadir Çakır

#TODO
#!RANSAC
#!Triangulation Network
#!Trilateration Network
#!GPS Network
#?Geoid Model
#?Web 
from cProfile import label
from CommonNet.Observation import ObservationNET
from CommonNet.Point import PointNET
from CommonNet.Baseline import BaselineNET
from CommonNet.Network import NetworkNET
from LevelNet.Level import LevelNET
from matplotlib import pyplot as plt

level=LevelNET(False,"Sample_Net",True)

P1=PointNET.FromCoordinates("P1",0.0,0.0,0.0)
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
print("RMSE {:.2f}".format(level.SLS.m0))



ObsTitle=[]
PointTitle=[]
Heights=[]
for i in level.Points:
    if (not i.IsFixed):
        PointTitle.append(i.name)
        Heights.append(i.Z)
for i in level.ValidObservations:
    ObsTitle.append(i.From.name+" to "+i.To.name)



plt.title("Estimated Elevations")
plt.plot(PointTitle,Heights)
plt.show()
plt.clf()

plt.title("Residuals")
plt.plot(ObsTitle,level.SLS.v)
plt.show()
plt.clf()
plt.title("Mean Error of Adjusted Parameters")
plt.plot(PointTitle,level.SLS.mxx)
plt.show()
plt.clf()
plt.title("Mean Error of Observations")
plt.plot(ObsTitle,level.SLS.ml)
plt.show()
plt.clf()
plt.title("Mean Error of Adjusted Observations")
plt.plot(ObsTitle,level.SLS.mL)
plt.show()
plt.clf()
plt.title("Mean Error of Residuals")
plt.plot(ObsTitle,level.SLS.mv)
plt.show()
plt.clf()
plt.title("Adjusted Observations")
plt.plot(ObsTitle,level.SLS.L,"b" , label="Adjusted Observations")
plt.plot(ObsTitle,level.SLS.l,"r" , label="Reduced Observations")
plt.legend()
plt.show()
plt.clf()
