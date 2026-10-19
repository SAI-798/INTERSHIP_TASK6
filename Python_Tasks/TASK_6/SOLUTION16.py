
# Problem: Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
