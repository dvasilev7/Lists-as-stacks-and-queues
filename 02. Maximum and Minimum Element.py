count_of_seq = int(input())

stack = []
for seq in range(count_of_seq):
    query_input = input().split()
    command = query_input[0]
    if command == "1":  # push second element to stack
        stack.append(int(query_input[1]))
    if len(stack) > 0:
        if command == "2":  # delete last element of stack
            stack.pop()
        elif command == "3":  # print maximum element
            print(max(stack))
        elif command == "4":  # print minimum element
            print(min(stack))

stack_reversed = []
for index in range(len(stack)):
    stack_reversed.append(str(stack.pop()))

print(", ".join(stack_reversed))
