x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
xs, ys = map(int, input().split())
u = int(input())

if ((abs(xs-x1)**2 + abs(ys-y1)**2)**0.5 <= u) | ((abs(xs-x2)**2 + abs(ys-y2)**2)**0.5 <= u):
    print("Yes")
else:
    print("No")