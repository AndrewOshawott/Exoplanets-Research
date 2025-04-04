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
sim.add(m=0.99)
#2433.08 //
sim.add(m=(1.206**3.7)/332946,P=3.37375965,theta=4.570633485340458,inc=89.2301*pi/180)
#2433.06 //
sim.add(m=(1.441**3.7)/332946,P=6.0632531,theta=1.4671656358462002,inc=89.5913*pi/180)
#2433.02 //
sim.add(m=(2.313**3)/332946, P=10.04380879,theta=0.7738833885841387,inc=89.531*pi/180)
#2433.01 //
sim.add(m=(2.361**3)/332946, P=15.16213142,theta=2.099350725353972,inc=89.2315*pi/180)
#2433.04 //
sim.add(m=(1.903**3)/332946, P=27.90426394,theta=5.033865022383818,inc=89.8041*pi/180)
#2433.03 //
sim.add(m=(2.423**3)/332946, P=56.41581418,theta=0.7675597641698175,inc=89.8225*pi/180)
#2433.07 //
sim.add(m=(2.252**3)/332946, P=86.43086179,theta=5.687372392604169,inc=89.9083*pi/180)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 3

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[5].l,sim.particles[6].l,sim.particles[7].l
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
ax.set_title("Resonant Argument of KOI 2433$_2$ (aka Kepler-385)",fontsize=20)
ax.annotate("p = 1, q = 3",xy=(9,365))
plt.figtext(0.05, 0.01, "2: This is a 7 planet system, this graph is for $\lambda_1$ = KOI 2433.04, $\lambda_2$ = KOI 2433.03, and $\lambda_3$ = KOI 2433.07", ha="left", fontsize=8)
plt.savefig("phichart2433_2.png")

