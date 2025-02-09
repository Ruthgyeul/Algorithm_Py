rs = []

while True:
    text = input()
    if text == ".":
        print("\n".join(rs))
        break

    stack = []
    balance = True

    for ele in text:
        if ele in "([":
            stack.append(ele)
        elif ele == ")":
            if not stack or stack[-1] != "(":
                balance = False
                break
            stack.pop()
        elif ele == "]":
            if not stack or stack[-1] != "[":
                balance = False
                break
            stack.pop()

    if balance and not stack:
        rs.append("yes")
    else:
        rs.append("no")