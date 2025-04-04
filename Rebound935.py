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
#935.04 //
sim.add(m=(1.888**3)/332946,P=9.61727175,theta=1.6085053573885446,inc=89.7234*pi/180)
#935.01 //
sim.add(m=(5.336**3)/332946,P=20.86019269,theta=6.1191878541641636,inc=89.668*pi/180)
#935.02 //
sim.add(m=(5.05**3)/332946, P=42.63416415,theta=3.49007552761808,inc=89.9429*pi/180)
#935.03 //
sim.add(m=(3.908**3)/332946, P=87.64796817,theta=0.7798040259361261,inc=89.9295*pi/180)


os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 1, 2

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
ax.set_title("Resonant Argument of KOI 935 (aka Kepler-31)",fontsize=20)
ax.annotate("p = 1, q = 2",xy=(9,365))
#plt.figtext(0.05, 0.01, "2: This is a 7 planet system, this graph is for $\lambda_1$ = KOI 2433.04, $\lambda_2$ = KOI 2433.03, and $\lambda_3$ = KOI 2433.07", ha="left", fontsize=8)
plt.savefig("phichart935.png")

