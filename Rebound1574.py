import rebound
from numpy import *
import matplotlib.pyplot as plt

sim = rebound.Simulation()

Mearth = 1.0/332940.0
GMsun = 1.3271244e20 # [m3 s-2]
au = 149597870700.0 # [m]
G = GMsun*(86400**2)/au**3 # au, days, Msun

sim.units = ('days','AU','Msun')
print(sim.G)

#star/COM
sim.add(m=1.02)
#1574.03 // Start with innermost planet, go outwards
sim.add(m=(1.649**3)/332946,P=5.83391524,theta=2.8266122994678042)
#1574.04 // Period is in days, convert to years (Divide by 365.2425)
sim.add(m=(1.403**3)/332946,P=8.97721049,theta=3.0445136870582044)
#1574.01 // mass ≈ R_p ^ 3 in Earth masses if radius of planet > 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1**3.7)/332946, P=114.7366498,theta=5.923396073788196)
#1574.02
sim.add(m=(1**3.7)/332946,P=191.2388431,theta=5.858135369155586)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 365*1000
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 3,5

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i] = sim.particles[3].l,sim.particles[4].l
sim.move_to_com()

#radian to degree conversion
phi_degrees = (phi*180/pi) % 360
print(phi_degrees)

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times,l1*180/pi, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (days)", fontsize=20)
ax.set_ylabel("$\lambda_1$ (degrees)", fontsize=20)
ax.set_title("Mean longitude of KOI 1574.01",fontsize=20)
plt.axhline(y=(5.923396073788196*180/pi), color='b', linestyle='--')
ax.plot([0,114.7366498],[5.923396073788196*180/pi,5.923396073788196*180/pi],'bo')
ax.annotate("(0,339.4$\degree$)",xy=(-5,325),color='b')
ax.annotate("(114.7366498,339.4$\degree$)",xy=(100,325),color='b')
#ax.legend(fontsize=24)
plt.savefig("lamdbachart1574.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,(3*l1*180/pi-5*l2*180/pi) % 360, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$p*\lambda_1 - q*\lambda_2$ (degrees)", fontsize=20)
#ax.legend(fontsize=24)
ax.set_title("Mean longitude of KOI 1574.01 - KOI 1574.02",fontsize=20)
ax.annotate("p = 3, q = 5",xy=(9,365))
plt.savefig("lamdbaequationchart1574.png")

for p in sim.particles:
    print("x/y values of each particle:", p.x, p.y)
for o in sim.orbits():
    print("orbit properties:", o)

