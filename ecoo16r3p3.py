import sys

input = sys.stdin.readline
w = int(input())
print(w)
words = set()
data = {}

for i in range(w):
    cw = input().strip()
    words.add(cw)
print(len(words))

for i in range(4):
    test = input().strip()
    if (test in words):
        print(0)
    else:
        cap = 0
        start = 0
        end = 2
        while (end < len(test)):
            print(test[start:end])
            if test[start:end] in data:
                cap += 1
                start = end
            end += 1
        print(cap)
