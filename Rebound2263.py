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
sim.add(m=1.22)
#2263.02 //
sim.add(m=(2.344**3)/332946,P=9.47852438,theta=3.5965797248025417,inc=89.3165*pi/180)
#2263.03 //
sim.add(m=(1.691**3)/332946,P=15.59458181,theta=1.9908343410591076,inc=89.528*pi/180)
#2263.01 //
sim.add(m=(3.043**3)/332946, P=29.96864759,theta=2.068041391900808,inc=89.6134*pi/180)


os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 3, 4

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

#radian to degree conversion
phi_degrees = (phi*180/pi) % 360
print(phi_degrees)

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 2263 (aka Kepler-1165)",fontsize=20)
ax.annotate("p = 3, q = 4",xy=(9,365))
#plt.figtext(0.05, 0.01, "2: This is a 5 planet system, this graph is for $\lambda_1$ = KOI 707.01, $\lambda_2$ = KOI 707.03, and $\lambda_3$ = KOI 707.02", ha="left", fontsize=8)
plt.savefig("phichart2263.png")

