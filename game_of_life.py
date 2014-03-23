from eco_system import *
from eco_system_renderer import *

size = 20
generations = 30

system = EcoSystem(size)

system.seed()

render_system(system)

for generation in range(0, generations):
  system.advance_generation()
  render_system(system)