
# Problem: String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

n = int(input())
width = len(format(n, "b"))

for i in range(1, n + 1):
    print(
        str(i).rjust(width),
        format(i, "o").rjust(width),
        format(i, "X").rjust(width),
        format(i, "b").rjust(width)
    )
