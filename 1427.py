def sortQ(text):
    if len(text) <= 1:
        return text

    pivot = text[-1]
    left = []
    right = []

    for char in text[:-1]:
        if char < pivot:
            left.append(char)
        else:
            right.append(char)

    return sortQ(right) + [pivot] + sortQ(left)

num = input()

print("".join(sortQ(num)))