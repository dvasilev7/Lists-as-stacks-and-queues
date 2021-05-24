from collections import deque

quantity = int(input())
seq = input().split()
queue = deque()

for index in range(len(seq)):
    queue.append(int(seq[index]))

print(max(queue))

for i in range(len(queue)):
    order = queue.popleft()
    if quantity - order >= 0:
        quantity -= order
    else:
        queue.appendleft(order)
        break

if len(queue) == 0:
    print("Orders complete")
else:
    print(f"Orders left:", " ".join([str(order) for order in queue]))