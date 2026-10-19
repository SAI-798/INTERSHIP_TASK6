
# Problem: Write a Function
# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = int(input())
print(is_leap(year))
