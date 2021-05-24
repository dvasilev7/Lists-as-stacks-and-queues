numbers = input().split()
stack = []
for index in range(len(numbers)):
    stack.append(numbers.pop())

print(" ".join(stack))