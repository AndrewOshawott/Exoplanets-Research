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

labels = ["Jupiter", "Io", "Europa","Ganymede","Callisto"]
#star/COM
sim.add(m=317.906)
#Io // Start with innermost planet, go outwards
sim.add(m=0.015,P=1.769137786, e=0.00472,inc=0.000654498469)
#Europa //
sim.add(m=0.008,P=3.551181, e=0.00981,inc=0.0080634211)
#Ganymede //
sim.add(m=0.025, P=7.15455296, e=0.00146,inc=0.0036128316)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 10000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 2

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = (p*l1[i])-((p+q)*l2[i])+(q*l3[i])
sim.move_to_com()

phi_degrees = (phi*180/pi) % 360

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue", figsize=[5.5,5])
op.ax.set_title("Jupiter Test")

labels = ["Jupiter", "Io", "Europa", "Ganymede"]
for i, p in enumerate(sim.particles):
    x, y, _ = p.xyz
    op.ax.text(x-0.0115, y+0.006, labels[i], fontsize=8, color="black")

op.fig.savefig("orbittest.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of Jupiter's Moons (Io, Europa, Ganymede)",fontsize=20)
ax.annotate("p = 1, q = 2",xy=(17.95,365.25))
#plt.figtext(0.05, 0.01, "1: This is a 5 planet system, this graph is for $\lambda_1$ = KOI 1151.01, $\lambda_2$ = KOI 1151.04, and $\lambda_3$ = KOI 1151.05", ha="left", fontsize=8)
plt.savefig("phichartTEST.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times,l1*180/pi, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (days)", fontsize=20)
ax.set_ylabel("$\lambda_1$ (degrees)", fontsize=20)
ax.set_title("Mean longitude of Io",fontsize=20)
plt.axhline(y=(3.3755376844593314*180/pi), color='b', linestyle='--')
ax.plot([0,5.24969846],[3.3755376844593314*180/pi,3.3755376844593314*180/pi],'bo')
ax.annotate("(0,193.4$\degree$)",xy=(-0.4,180),color='b')
ax.annotate("(5.24969846,193.4$\degree$)",xy=(5.2,180),color='b')
plt.savefig("lamdbachartTEST.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,(1*l2*180/pi-2*l3*180/pi) % 360, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$p*\lambda_1 - q*\lambda_2$ (degrees)", fontsize=20)
ax.set_title("Mean longitude of Io - Europa",fontsize=20)
ax.annotate("p = 1, q = 2",xy=(9,365.25))
plt.savefig("lamdbaequationchartTEST.png")
