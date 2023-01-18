def truck_tour(petrol_pumps):
    remaining_fuel = 0
    start = 0
    for i in range(len(petrol_pumps)):
        fuel, dist = petrol_pumps[i]
        remaining_fuel += fuel - dist
        if remaining_fuel < 0:
            remaining_fuel = 0
            start = i + 1
    return start
