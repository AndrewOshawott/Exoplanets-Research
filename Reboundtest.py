import rebound

sim = rebound.Simulation()
rebound.data.add_solar_system(sim)

sim.integrate(1000)

op = rebound.OrbitPlot(sim,unitlabel="[AU]", color="blue")
op.fig.savefig("solarsystem.png")

for p in sim.particles:
    print(p.x, p.y, p.z)
for o in sim.orbits():
    print(o)