
# Problem: Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english - french))
