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
sim.add(m=0.72)
#82.05
sim.add(m=(0.461**3.7)/332946,P=5.28689179,theta=3.2085719063511213,inc=89.5727*pi/180)
#82.04
sim.add(m=(0.575**3.7)/332946,P=7.07134469,theta=6.172843245945866,inc=89.5665*pi/180)
#82.02
sim.add(m=(1.177**3.7)/332946, P=10.31172605,theta=0.8588212813298691,inc=89.8327*pi/180)
#82.01
sim.add(m=(2.175**3)/332946,P=16.14567465,theta=0.7143358236451717,inc=89.9221*pi/180)
#82.06
sim.add(m=(0.601**3.7)/332946,P=22.4100071,theta=1.3765363991299924,inc=89.9299*pi/180)
#82.03
sim.add(m=(0.833**3)/332946,P=27.45362377,theta=3.5773297938781012,inc=89.8632*pi/180)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 4, 7

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[3].l,sim.particles[4].l,sim.particles[5].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

#radian to degree conversion
phi_degrees = (phi*180/pi) % 360

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 82 (aka Kepler-102)",fontsize=20)
ax.annotate("p = 4, q = 7",xy=(9,365))
plt.savefig("phichart82.png")