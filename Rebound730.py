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
sim.add(m=1.04)
#730.04 // Start with innermost planet, go outwards
sim.add(m=(2.932**3)/332946,P=7.38445597,theta=0.5270963547326541,inc=89.6208*pi/180)
#730.02 // mass ≈ R_p ^ 3 in Earth masses if radius of planet > 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(3.314**3)/332946,P=9.84821114,theta=5.988694195771712,inc=89.6128*pi/180)
#730.01 //
sim.add(m=(4.416**3)/332946, P=14.78701236,theta=2.0229457548913903,inc=89.6931*pi/180)
#730.03
sim.add(m=(3.807**3)/332946,P=19.72433675,theta=0.5940821662410035,inc=89.708*pi/180)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 2, 4

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[2].l,sim.particles[3].l,sim.particles[4].l
    phi[i] = p*l1[i]-(p+q)*l2[i]+q*l3[i]
sim.move_to_com()

#radian to degree conversion
phi_degrees = (phi*180/pi) % 360
print(phi_degrees)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue", figsize=[5.5,5])
op.ax.set_title("KOI 730 (aka Kepler-223)")

fig = plt.figure(figsize=(9,7))
ax = plt.subplot(111)
ax.plot(times/365.2425,phi_degrees, 'b', marker=".", markersize=.5)
ax.set_xlabel("t (years)", fontsize=20)
ax.set_ylabel("$\Phi$ (degrees)", fontsize=20)
ax.set_title("Resonant Argument of KOI 730$_2$ (aka Kepler-223)",fontsize=20)
ax.annotate("p = 2, q = 4",xy=(9,365))
plt.figtext(0.05, 0.01, "2: This is a 4 planet system, this graph is for $\lambda_1$ = KOI 730.02, $\lambda_2$ = KOI 730.01, and $\lambda_3$ = KOI 730.03", ha="left", fontsize=8)
plt.savefig("phichart730_2.png")

