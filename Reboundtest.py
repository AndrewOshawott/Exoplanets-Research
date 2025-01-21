import rebound

sim = rebound.Simulation()

sim.units = ('yr','AU','Msun')

#star/COM
sim.add(m=0.83)
#1151.01
sim.add(a=(23.1754*.85))
#1151.02
sim.add(a=(17.2046*.85))
#1151.03
sim.add(a=(14.4239*.85))
#1151.04
sim.add(a=(32.4377*.85))
#1151.05
sim.add(a=(36.9346*.85))

sim.integrate(1000)

sim.status()