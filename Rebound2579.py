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
sim.add(m=1.1)
#2579.01 //
sim.add(m=(1.302**3.7)/332946,P=2.72960744,theta=2.9629138614644255,inc=89.2156*pi/180)
#2579.02 //
sim.add(m=(1.329**3.7)/332946,P=3.59647062,theta=3.7232636039355533,inc=89.2948*pi/180)
#2579.03 //
sim.add(m=(1.394**3.7)/332946, P=10.30132666,theta=0.80302957727453,inc=89.5879*pi/180)


os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 6, 3

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
ax.set_title("Resonant Argument of KOI 2579 (aka Kepler-1859)",fontsize=20)
ax.annotate("p = 6, q = 3",xy=(9,365))
#plt.figtext(0.05, 0.01, "2: This is a 5 planet system, this graph is for $\lambda_1$ = KOI 707.01, $\lambda_2$ = KOI 707.03, and $\lambda_3$ = KOI 707.02", ha="left", fontsize=8)
plt.savefig("phichart2579.png")

