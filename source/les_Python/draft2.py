
from collections import deque

a = deque([4,5,6])

a.popleft()
a.append(7)

print(a)
if a:
    print("puste")

a.popleft()
a.popleft()
a.popleft()

if a:
    print("puste2")


stack = [4,5,6]
stack.pop()
stack.append(7)
print(stack)


