from eco_system import *

def run_neighbour_count_test(target, expected):
  actual = target.number_of_neighbours(1,1)
  if actual != expected:
    raise ValueError("expected {0} neighbour(s) but found {1}".format(expected, actual))

def run_next_generation_cell_state_test(target, expected):
  actual = target.next_generation_cell_state(1,1)
  if actual != expected:
    raise ValueError("expected {0} but got {1}".format(expected, actual))


def test_neighbour_count():
  target = EcoSystem(4)

  target.set_alive(0,0)
  run_neighbour_count_test(target, 1)

  target.set_alive(1,0)
  run_neighbour_count_test(target, 2)

  # ensure ignores middle cell
  target.set_alive(1,1)
  run_neighbour_count_test(target, 2)

  target.set_alive(1,2)
  run_neighbour_count_test(target, 3)

  # ensure ignores cells outside range
  target.set_alive(3,2)
  run_neighbour_count_test(target, 3)

  print("#test_neighbour_count passed")


def test_next_generation_cell_state():
  # dead cell
  target = EcoSystem(4)
  target.set_dead(1,1)

  # 2 neighbours
  target.set_alive(0,0)
  target.set_alive(0,1)
  run_next_generation_cell_state_test(target, 0)

  # 3 neighbours
  target.set_alive(0,2)
  run_next_generation_cell_state_test(target, 1)

  # 4 neighbours
  target.set_alive(1,0)
  run_next_generation_cell_state_test(target, 0)


  # live cell
  target = EcoSystem(4)
  target.set_alive(1,1)

  # 1 neighbour
  target.set_alive(0,0)
  run_next_generation_cell_state_test(target, 0)

  # 2 neighbours
  target.set_alive(1,0)
  run_next_generation_cell_state_test(target, 1)

  # 3 neighbours
  target.set_alive(2,0)
  run_next_generation_cell_state_test(target, 1)

  # 4 neighbours
  target.set_alive(2,1)
  run_next_generation_cell_state_test(target, 0)

  print("#test_next_generation_cell_state passed")


test_neighbour_count()
test_next_generation_cell_state()