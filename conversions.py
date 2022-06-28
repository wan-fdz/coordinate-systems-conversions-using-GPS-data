""" coordinate-systems-conversions-using-GPS-data.py

    Author: Vanessa Fernández
    Contact: vfernandezv6@gmail.com
    First created: 09/19/20
    Last updated: 09/25/20
"""

#Import standard libraries
import math
import numpy as np

rea = 6378137 #Semi-major axis (parameter associated with geodetic frame)
e = 0.08181919 #First eccentricity (parameter associated with geodetic frame)

#Test data provided by professor in class
#pg_p0 = np.array([math.radians(-100.3750282), math.radians(25.7188255), 100])
#pg_p1 = np.array([math.radians(-100.3746785), math.radians(25.7188838), 100])

#Data provided in the lab instructions
pg_p0 = np.array([math.radians(-100.417281), math.radians(25.663137), 100])
pg_p1 = np.array([math.radians(-100.416584), math.radians(25.663058), 100])

#Calculation of the prime vertical radius of curvature for P0 and P1 
#(parameter associated with geodetic frame)
Ne_p0 = rea / math.sqrt(1 - ((e**2)*(math.sin(pg_p0[1])**2)))
Ne_p1 = rea / math.sqrt(1 - ((e**2)*(math.sin(pg_p1[1])**2)))


#Coordinates for the reference point (P0) in the ECEF frame
Pe_ref = np.array([[(Ne_p0 + pg_p0[2])*math.cos(pg_p0[1])*math.cos(pg_p0[0])],
                   [(Ne_p0 + pg_p0[2])*math.cos(pg_p0[1])*math.sin(pg_p0[0])],
                   [((Ne_p0*(1-e**2))+ pg_p0[2])*math.sin(pg_p0[1])]])

#Coordinates for P1 in the ECEF frame
Pe = np.array([[(Ne_p1 + pg_p1[2])*math.cos(pg_p1[1])*math.cos(pg_p1[0])],
               [(Ne_p1 + pg_p1[2])*math.cos(pg_p1[1])*math.sin(pg_p1[0])],
               [((Ne_p1*(1-e**2))+ pg_p1[2])*math.sin(pg_p1[1])]])

#Print the value of the ECEF coordinates calculated for both points
print("\n")
print("--------------------------------------------------------")
print("         Earth-centered Earth-Fixed Coordinates         ")
print("--------------------------------------------------------")
print("         X(m)              Y(m)              Z(m)   ")
for i in Pe_ref:
    print(i,end = ' ')
print("\n")
for i in Pe:
    print(i,end = ' ')

#Calculation of the rotation matrix from the ECEF frame to the local NED frame
Rne = np.array([[-math.sin(pg_p0[1])*math.cos(pg_p0[0]), -math.sin(pg_p0[1])*math.sin(pg_p0[0]), math.cos(pg_p0[1])],
                [-math.sin(pg_p0[0]), math.cos(pg_p0[0]), 0],
                [-math.cos(pg_p0[1])*math.cos(pg_p0[0]), -math.cos(pg_p0[1])*math.sin(pg_p0[0]), -math.sin(pg_p0[1])]])

#Complete position conversion from the geodetic to local NED frame
Pn = np.dot(Rne,(Pe - Pe_ref))


#Print the value of the NED coordinates calculated
print("\n")
print("--------------------------------------")
print("        Coordinates in NED            ")
print("--------------------------------------")
print("    North          East         Down  ")
for i in Pn:
    print(i,end = ' ')
print("\n")
