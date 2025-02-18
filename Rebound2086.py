import rebound
from numpy import *
import matplotlib.pyplot as plt

sim = rebound.Simulation()

sim.units = ('yr','AU','Msun')

#star/COM
sim.add(m=1)
#2086.01 // Start with innermost planet, go outwards
sim.add(m=(1.734**3)/332946,P=7.13295045/365.2425,theta=10.300453650942318)
#2086.02 // Period is in days, convert to years (Divide by 365.2425)
sim.add(m=(1.943**3)/332946,P=8.91897737/365.2425,theta=7.303898735779818)
#2086.03 // mass ≈ R_p ^ 3 in Earth masses if radius of planet > 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1.756**3)/332946, P=11.89824703/365.2425,theta=12.686669555423437)
#2086.04
sim.add(m=(1.836**3)/332946,P=335.5198537/365.2425,theta=-170.78681528312197)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 100
Nout = 365*Tfinal # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 1

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[1].l,sim.particles[2].l,sim.particles[3].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

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
ax.plot(times,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years) ", fontsize=24)
ax.set_ylabel("\u03C6 (deg)", fontsize=24)
ax.legend(fontsize=24)
plt.savefig("phichart2086.png")

for p in sim.particles:
    print("x/y values of each particle:", p.x, p.y)
for o in sim.orbits():
    print("orbit properties:", o)

