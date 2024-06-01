class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        return f"{self.age} {self.name}"

n = int(input())
mList = []

for i in range(n):
    age, name = map(str, input().split())
    mList.append(Member(name, int(age)))
    
mList.sort(key=lambda member: member.age)

for ele in mList:
    print(ele.print())