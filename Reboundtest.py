import rebound

sim = rebound.Simulation()

sim.units = ('yr','AU','Mearth')

#star/COM, convert Msun to Mearth (multiply by 332946)
sim.add(m=0.83*332946)
#1151.01
sim.add(m=1, P=10.43545334)
#1151.02
sim.add(m=1,P=7.41088006)
#1151.03
sim.add(m=1,P=5.24969846)
#1151.04
sim.add(m=1,P=17.45319318)
#1151.05
sim.add(m=1,P=21.72027051)

sim.integrate(1000)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue")
op.fig.savefig("orbit.png")