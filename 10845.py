n = int(input())
queue = []
result = []

for _ in range(n):
    cmd = input().split()
    
    match cmd[0]:
        case "push":
            queue.append(int(cmd[1]))
        case "pop":
            if queue:
                result.append(queue.pop(0))
            else:
                result.append(-1)
        case "size":
            result.append(len(queue))
        case "empty":
            result.append(1 if not queue else 0)
        case "front":
            result.append(queue[0] if queue else -1)
        case "back":
            result.append(queue[-1] if queue else -1)

for ele in result:
    print(ele)
