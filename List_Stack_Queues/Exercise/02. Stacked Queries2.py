n = int(input())
stack = []
function  = {
    '1': lambda x: stack.append(int(x)) ,
    '2': lambda : stack.pop() if stack else None,
    '3': lambda : print(max(stack)) if stack else None,
    '4': lambda : print(min(stack)) if stack else None
}
for _ in range(n):
    command = input().split()
    function[command[0]](*command[1:])

print(*stack,sep=', ')

