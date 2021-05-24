stack = input().split()
rack = int(input())
rack_counter = 1


new_rack = rack
while len(stack) > 0:
    piece = int(stack.pop())
    if new_rack >= piece:
        new_rack -= piece
    else:
        stack.append(str(piece))
        rack_counter += 1
        new_rack = rack

print(rack_counter)