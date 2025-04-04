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
sim.add(m=1.11)
#351.06 //
sim.add(m=(1.286**3.7)/332946,P=7.00823625,theta=1.341619702093693,inc=89.4787*pi/180)
#351.05 //
sim.add(m=(1.513**3.7)/332946,P=8.71984892,theta=0.8460786481061584,inc=89.6753*pi/180)
#351.08 //
sim.add(m=(1.11**3.7)/332946, P=14.44913641,theta=2.9337216790003056,inc=89.8195*pi/180)
#351.03 //
sim.add(m=(2.843**3)/332946, P=59.73725869,theta=3.253400267614421,inc=89.9236*pi/180)
#351.04 //
sim.add(m=(2.623**3)/332946, P=91.9400901,theta=4.7235708677678945,inc=89.8698*pi/180)
#351.07 //
sim.add(m=(2.641**3)/332946, P=124.9218471,theta=4.660428011165902,inc=89.8626*pi/180)
#351.02 //
sim.add(m=(7.614**3)/332946, P=210.7307044,theta=2.031651532376542,inc=89.9909*pi/180)
#351.01 //
sim.add(m=(10.777**3)/332946, P=331.5973066,theta=0.8205787289222528,inc=89.9827*pi/180)

os = sim.orbits()
print("n_i (in rad/days) = %6.3f, %6.3f, %6.3f" % (os[0].n,os[1].n,os[2].n))
print("P_i (in days)     = %6.3f, %6.3f, %6.3f" % (os[0].P,os[1].P,os[2].P))

Tfinal= 10*365
Nout = 1000 # number of printed out timesteps.

phi = zeros(Nout)
l1,l2,l3 = zeros(Nout), zeros(Nout), zeros(Nout)

p,q = 3, 6

times = linspace(0.,Tfinal,Nout)
for i,time in enumerate(times):
    sim.integrate(time)
    l1[i],l2[i],l3[i] = sim.particles[6].l,sim.particles[7].l,sim.particles[8].l
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
ax.set_title("Resonant Argument of KOI 351$_3$ (aka Kepler-90)",fontsize=20)
ax.annotate("p = 3, q = 6",xy=(9,365))
plt.figtext(0.05, 0.01, "3: This is an 8 planet system, this graph is for $\lambda_1$ = KOI 351.07, $\lambda_2$ = KOI 351.02, and $\lambda_3$ = KOI 351.01", ha="left", fontsize=8)
plt.savefig("phichart351_3.png")

