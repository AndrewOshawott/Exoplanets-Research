import rebound

sim = rebound.Simulation()

sim.units = ('yr','AU','Msun')

#star/COM
sim.add(m=0.83)
#1151.01 // mass ≈ R_p ^ 3.7 in Earth masses if radius of planet < 1.7 earth radii, then divide by 332946 to convert to solar masses
sim.add(m=(1.229**3.7)/332946, P=10.43545334,theta=8.475163889910444)
#1151.02
sim.add(m=(0.948**3.7)/332946,P=7.41088006,theta=8.45398854570443)
#1151.03
sim.add(m=(0.672**3.7)/332946,P=5.24969846,theta=8.875948944787911)
#1151.04
sim.add(m=(0.759**3.7)/332946,P=17.45319318,theta=-1.8488879509549183)
#1151.05
sim.add(m=(0.801**3.7)/332946,P=21.72027051,theta=4.824742488707509)

sim.integrate(1000)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue")
op.ax.set_title("KOI 1151 (aka Kepler-271)")

labels = ["Star", "1151.01", "1151.02", "1151.03", "1151.04", "1151.05"]
for i, p in enumerate(sim.particles):
    x, y, _ = p.xyz
    op.ax.text(x-.55, y+.3, labels[i], fontsize=8, color="black")

op.fig.savefig("orbit.png")