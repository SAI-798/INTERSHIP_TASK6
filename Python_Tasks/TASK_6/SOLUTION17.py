
# Problem: Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
result = True

for _ in range(int(input())):
    b = set(map(int, input().split()))

    if not (a > b):
        result = False
        break

print(result)
