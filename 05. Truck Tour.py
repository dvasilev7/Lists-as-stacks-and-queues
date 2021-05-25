from collections import deque
n = int(input())

queue = deque()

for i in range(n):  # in order to put the petrol and the distance in queue
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for index in range(n):
    fuel_tank = 0
    travelled = 0
    for gas_pump in queue:
        fuel, distance = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance:     # can the truck start here
            break
        fuel_tank -= distance
        travelled += 1
    if travelled == len(queue):      # can the truck make a full circle
        print(index)
        break
    queue.rotate(-1)
