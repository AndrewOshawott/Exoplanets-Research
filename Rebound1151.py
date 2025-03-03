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
sim.add(m=0.83)
#1151.03 // Start with innermost planet, go outwards
sim.add(m=(0.672**3.7)/332946,P=5.24969846,theta=3.3755376844593314)
#1151.02 // Period is in days, convert to years (Divide by 365.2425)
sim.add(m=(0.948**3.7)/332946,P=7.41088006,theta=6.1176240098545245)
#1151.01 // mass ≈ R_p ^ 3.7 in Earth masses if radius of planet < 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1.229**3.7)/332946, P=10.43545334,theta=1.5428143395216987)
#1151.04
sim.add(m=(0.759**3.7)/332946,P=17.45319318,theta=0.7952049261151819)
#1151.05
sim.add(m=(0.801**3.7)/332946,P=21.72027051,theta=4.9711773818589755)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[2].n,os[3].n,os[4].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[2].P,os[3].P,os[4].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 7, 24

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[3].l,sim.particles[4].l,sim.particles[5].l
    phi[i] = p*l3[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

phi_degrees = (phi*180/pi) % 360

print(phi_degrees)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue", figsize=[5.5,5])
op.ax.set_title("KOI 1151 (aka Kepler-271)")

labels = ["Star", "1151.03", "1151.02", "1151.01", "1151.04", "1151.05"]
for i, p in enumerate(sim.particles):
    x, y, _ = p.xyz
    op.ax.text(x-0.0115, y+0.006, labels[i], fontsize=8, color="black")

op.fig.savefig("orbit1151.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 1151$_2$ (aka Kepler-271)",fontsize=20)
ax.annotate("p = 7, q = 24",xy=(8.95,365.25))
plt.figtext(0.05, 0.01, "1: This is a 5 planet system, this graph is for $\lambda_1$ = KOI 1151.01, $\lambda_2$ = KOI 1151.04, and $\lambda_3$ = KOI 1151.05", ha="left", fontsize=8)
plt.savefig("phichart1151.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times,l1*180/pi, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (days)", fontsize=20)
ax.set_ylabel("$\lambda_1$ (degrees)", fontsize=20)
ax.set_title("Mean longitude of KOI 1151.03",fontsize=20)
plt.axhline(y=(3.3755376844593314*180/pi), color='b', linestyle='--')
ax.plot([0,5.24969846],[3.3755376844593314*180/pi,3.3755376844593314*180/pi],'bo')
ax.annotate("(0,193.4$\degree$)",xy=(-0.4,180),color='b')
ax.annotate("(5.24969846,193.4$\degree$)",xy=(5.2,180),color='b')
#ax.legend(fontsize=24)
plt.savefig("lamdbachart1151.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,(4*l2*180/pi-5*l3*180/pi) % 360, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$p*\lambda_2 - q*\lambda_3$ (degrees)", fontsize=20)
#ax.legend(fontsize=24)
ax.set_title("Mean longitude of KOI 1151.04 - KOI 1151.05",fontsize=20)
ax.annotate("p = 4, q = 5",xy=(9,365.25))
plt.savefig("lamdbaequationchart1151.png")

for p in sim.particles:
    print("x/y values of each particle:", p.x, p.y)
for o in sim.orbits():
    print("orbit properties:", o)

