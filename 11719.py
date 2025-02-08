lines = []

try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    print("\n".join(lines))