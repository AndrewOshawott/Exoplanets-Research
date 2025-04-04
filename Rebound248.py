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
sim.add(m=0.61)
#248.03 //
sim.add(m=(1.811**3)/332946,P=2.5765741,theta=5.823860238089903,inc=89.7486*pi/180)
#248.01 //
sim.add(m=(2.606**3)/332946,P=7.20386128,theta=5.8921561423425635,inc=89.8555*pi/180)
#248.02 //
sim.add(m=(2.325**3)/332946, P=10.91276664,theta=0.3210910733623509,inc=89.7165*pi/180)
#248.04 //
sim.add(m=(1.777**3)/332946, P=18.59617273,theta=5.973690623811332,inc=89.9137*pi/180)


os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 20*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 4, 5

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[2].l,sim.particles[3].l,sim.particles[4].l
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
ax.set_title("Resonant Argument of KOI 248 (aka Kepler-49)",fontsize=20)
ax.annotate("p = 4, q = 5",xy=(18,365))
#plt.figtext(0.05, 0.01, "2: This is a 5 planet system, this graph is for $\lambda_1$ = KOI 707.01, $\lambda_2$ = KOI 707.03, and $\lambda_3$ = KOI 707.02", ha="left", fontsize=8)
plt.savefig("phichart248.png")

