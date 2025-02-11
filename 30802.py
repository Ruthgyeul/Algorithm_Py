n = int(input())  
ts = list(map(int, input().split()))  
t, p = map(int, input().split())  

rsT = sum((x + t - 1) // t for x in ts)  
print(rsT)  
print(n // p, n % p)  