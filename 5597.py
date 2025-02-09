total = set(range(1, 31))
st = {int(input()) for _ in range(28)}

print("\n".join(map(str, sorted(total - st))))