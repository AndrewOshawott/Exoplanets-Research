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
sim.add(m=1)
#2086.01 // Start with innermost planet, go outwards
sim.add(m=(1.734**3)/332946,P=7.13295045,theta=4.268962021689864)
#2086.02 // Period is in days, convert to years (Divide by 365.2425)
sim.add(m=(1.943**3)/332946,P=8.91897737,theta=1.6340637234308417)
#2086.03 // mass ≈ R_p ^ 3 in Earth masses if radius of planet > 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1.756**3)/332946, P=11.89824703,theta=6.145702704123614)
#2086.04
sim.add(m=(1.836**3)/332946,P=335.5198537,theta=3.1986270262231145)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 10000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 4, 4

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

#radian to degree conversion
phi_degrees = (phi*180/pi) % 360
print(phi_degrees)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue", figsize=[5.5,5])
op.ax.set_title("KOI 2086 (aka Kepler-60)")

labels = ["Star", "2086.01", "2086.02", "2086.03", "2086.04"]
for i, p in enumerate(sim.particles):
    x, y, _ = p.xyz
    op.ax.text(x-0.0115, y+0.006, labels[i], fontsize=8, color="black")

op.fig.savefig("orbit2086.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 2086 (aka Kepler-60)",fontsize=20)
ax.annotate("p = 4, q = 4",xy=(9,360))
#ax.legend(fontsize=24)
plt.savefig("phichart2086.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times,l1*180/pi, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (days) ", fontsize=20)
ax.set_ylabel("$\lambda_1$ (degrees)", fontsize=20)
ax.set_title("Mean longitude of KOI 2086.01",fontsize=20)
plt.axhline(y=(4.268962021689864*180/pi), color='b', linestyle='--')
ax.plot([0,7.13295045],[4.268962021689864*180/pi,4.268962021689864*180/pi],'bo')
ax.annotate("(0,244.6$\degree$)",xy=(-0.4,230),color='b')
ax.annotate("(7.13295045,244.6$\degree$)",xy=(7.1,230),color='b')
#ax.legend(fontsize=24)
plt.savefig("lamdbachart2086.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times,(4*l1*180/pi-4*l2*180/pi) % 360, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (days) ", fontsize=20)
ax.set_ylabel("$p*\lambda_1 - q*\lambda_2$ (degrees)", fontsize=20)
#ax.legend(fontsize=24)
ax.set_title("Mean longitude of KOI 2086.01 - KOI 2086.02",fontsize=20)
ax.annotate("p = 4, q = 4",xy=(27.25,365))
plt.savefig("lamdbaequationchart2086.png")

for p in sim.particles:
    print("x/y values of each particle:", p.x, p.y)
for o in sim.orbits():
    print("orbit properties:", o)

