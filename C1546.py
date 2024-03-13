subject = int(input())
score = [int(e) for e in input().split()]
total = 0

score.sort()

for i in range(subject):
    total +=  int(score[i])/int(score[-1]) * 100

print(total/subject)