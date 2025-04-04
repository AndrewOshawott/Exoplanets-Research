import rebound
from numpy import *
import matplotlib.pyplot as plt

sim = rebound.Simulation()

Mearth = 1.0/332940.0
GMsun = 1.3271244e20 # [m3 s-2]
au = 149597870700.0 # [m]
G = GMsun*(86400**2)/au**3 # au, days, Msun

sim.units = ('day','AU','Msun')
print(sim.G)

#star/COM
sim.add(m=0.73)
#500.05
sim.add(m=(1.414**3.7)/332946,P=0.98678597,theta=2.4355621644187977, inc=89.1374*pi/180)
#500.03
sim.add(m=(1.573**3.7)/332946,P=3.07215234,theta=0.4740243350522775, inc=89.7348*pi/180)
#500.04
sim.add(m=(1.607**3.7)/332946, P=4.64539336,theta=2.2549978802066732, inc=89.7485*pi/180)
#500.01
sim.add(m=(2.596**3)/332946,P=7.05352865,theta=0.39262493210667415, inc=89.7896*pi/180)
#500.02
sim.add(m=(2.606**3)/332946,P=9.52164568,theta=1.9798779654977992,inc=89.832*pi/180)
#500.06
sim.add(m=(1.235**3.7)/332946,P=14.64538173,theta=2.89534062457073, inc=89.8994*pi/180)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[2].n,os[3].n,os[4].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[2].P,os[3].P,os[4].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 6

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

phi_degrees = (phi*180/pi) % 360

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 500$_3$ (aka Kepler-80)",fontsize=20)
ax.annotate("p = 1, q = 6",xy=(9,275))
plt.figtext(0.05, 0.01, "3: This is a 6 planet system, this graph is for $\lambda_1$ = KOI 500.05, $\lambda_2$ = KOI 500.03, and $\lambda_3$ = KOI 500.04", ha="left", fontsize=8)
plt.savefig("phichart500_1.png")

