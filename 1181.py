def sort(words):
    words = list(set(words))
    words.sort(key=lambda word: (len(word), word))
    return words

n = int(input())
words = [input() for _ in range(n)]

print("\n".join(sort(words)))