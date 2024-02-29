num = input().split(" ")
n1 = int(num[0])
n2 = int(num[1])

list1 = []
list2 = []
result = []

for i in range(n1 + n2):
    if i <= n1: 
        name = input()
        list1.append(name)
    else:
        name = input()
        list2.append(name)

list1.sort()

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            result.append(list1[i])

print(len(result))
for e in result:
    print(e)