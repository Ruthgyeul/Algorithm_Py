report = []
hakjumT, score = 0, 0

point = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0
}

for _ in range(20):
    subj = input().split()
    report.append(subj)

for subj in report:
    hakjum = float(subj[1])
    rate = subj[2]
    if rate != "P":
        hakjumT += hakjum
        score += point.get(rate, 0) * hakjum

print("{:.6f}".format(score / hakjumT))