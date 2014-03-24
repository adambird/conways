from eco_system import *
from eco_system_renderer import *
import time

size = 40
generations = 300

system = EcoSystem(size)

system.seed()

render_system(system)

for generation in range(0, generations):
  system.advance_generation()
  render_system(system)
  time.sleep(0.1)
