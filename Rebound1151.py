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
sim.add(m=0.83)
#1151.03 // Start with innermost planet, go outwards
sim.add(m=(0.672**3.7)/332946,P=5.24969846,theta=3.3755376844593314)
#1151.02 // Period is in days, convert to years (Divide by 365.2425)
sim.add(m=(0.948**3.7)/332946,P=7.41088006,theta=6.1176240098545245)
#1151.01 // mass ≈ R_p ^ 3.7 in Earth masses if radius of planet < 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1.229**3.7)/332946, P=10.43545334,theta=1.5428143395216987)
#1151.04
#sim.add(m=(0.759**3.7)/332946,P=17.45319318/365.2425,theta=-1.8488879509549183)
#1151.05
#sim.add(m=(0.801**3.7)/332946,P=21.72027051/365.2425,theta=4.824742488707509)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 365
Nout = 100 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 5, 7

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
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
ax.set_xlabel("t (years) ", fontsize=24)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=24)
ax.legend(fontsize=24)
plt.savefig("phichart1151.png")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,l1, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years) ", fontsize=24)
ax.set_ylabel("$\lambda_1$ (AU)", fontsize=24)
ax.legend(fontsize=24)
plt.savefig("lamdbachart1151.png")

for p in sim.particles:
    print("x/y values of each particle:", p.x, p.y)
for o in sim.orbits():
    print("orbit properties:", o)

