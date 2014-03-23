def render_system(system):
    print("START System")
    # print(system.rows)
    for y in range(system.size):
        row = ""
        for x in range(system.size):
            # print(system.cell_state(x,y))
            if system.cell_state(x,y) == 0:
                cell = "-"
            else:
                cell = "X"
            row = row + cell

        print(row)
    print("END system")