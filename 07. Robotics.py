from collections import deque


def convert(s):
    s = s % (24 * 3600)
    hour = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return "%02d:%02d:%02d" % (hour, m, s)


robots = input().split(";")
robots_queue = deque()

for i in range(len(robots)):
    name, proc_time = robots[i].split("-")
    robots_queue.append([name, proc_time])

products_queue = deque()

starting_time = input().split(":")

command = input()
while command != "End":
    products_queue.append(command)
    command = input()


hours = int(starting_time[0])
minutes = int(starting_time[1])
seconds = int(starting_time[2])
time_in_sec = (hours * 3600) + (minutes * 60) + seconds
current_time = time_in_sec

is_processed = True
while len(products_queue) > 0:
    current_time += 1
    current_product = products_queue.popleft()
    for robot in range(len(robots_queue)):
        det_robot = robots_queue.popleft()
        name = det_robot[0]
        proc_time = int(det_robot[1])
        end_time = 0
        if len(det_robot) == 3:
            end_time = det_robot[2]
        if current_time >= end_time:
            end_time = current_time + proc_time
            is_processed = True
            print(f"{name} - {current_product} [{convert(current_time)}]")
            robots_queue.append([name, proc_time, end_time])
            break
        else:
            is_processed = False
            robots_queue.append([name, proc_time, end_time])
    if not is_processed:
        products_queue.append(current_product)
