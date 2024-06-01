def draw(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    else:
        stars = draw(n // 2)
        top = [' ' * (n // 2) + star + ' ' * (n // 2) for star in stars]
        bottom = [star + ' ' + star for star in stars]
        return top + bottom

def result(n):
    stars = draw(n)
    for star in stars:
        print(star)


n = int(input())
result(n)
