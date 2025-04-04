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
sim.add(m=0.7)
#2045.01 //
sim.add(m=(1.704**3)/332946,P=5.47665173,theta=5.514879981763534,inc=89.6931*pi/180)
#2045.03 //
sim.add(m=(1.264**3.7)/332946,P=16.93512559,theta=5.725208237329407,inc=89.7786*pi/180)
#2045.02 //
sim.add(m=(1.423**3.7)/332946, P=24.2095264,theta=0.8927779025077038,inc=89.8158*pi/180)


os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 7

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
ax.set_title("Resonant Argument of KOI 2045 (aka Kepler-354)",fontsize=20)
ax.annotate("p = 1, q = 7",xy=(9,365))
#plt.figtext(0.05, 0.01, "2: This is a 7 planet system, this graph is for $\lambda_1$ = KOI 2433.04, $\lambda_2$ = KOI 2433.03, and $\lambda_3$ = KOI 2433.07", ha="left", fontsize=8)
plt.savefig("phichart2045.png")

