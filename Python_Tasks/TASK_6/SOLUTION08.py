
# Problem: Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())
numbers = tuple(map(int, input().split()))

print(hash(numbers))
