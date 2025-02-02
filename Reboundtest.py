import rebound

sim = rebound.Simulation()

sim.units = ('yr','AU','Msun')

#star/COM, convert Msun to Mearth (multiply by 332946)
sim.add(m=0.83)
#1151.01
sim.add(m=1/332946, P=10.43545334,theta=8.475163889910444)
#1151.02
sim.add(m=1/332946,P=7.41088006,theta=8.45398854570443)
#1151.03
sim.add(m=1/332946,P=5.24969846,theta=8.875948944787911)
#1151.04
sim.add(m=1/332946,P=17.45319318,theta=-1.8488879509549183)
#1151.05
sim.add(m=1/332946,P=21.72027051,theta=4.824742488707509)

sim.integrate(1000)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue")
op.fig.savefig("orbit.png")