##鄂尔勒克 18377370
d = int(input())
n = int(input())
a = []
j = 0
while j < n:
    x0,y0,k0 = map(int,input().split())
    a.append((x0,y0,k0))
    j += 1
s = 0
w2 = 0
for x0 in range(129):
    for y0 in range(129):
        w1 = 0
        for p in a:
            if x0 - d <= p[0] <= x0 + d:
                if y0 - d <= p[1] <= y0 + d:
                    w1 = w1+p[2]
        if w1 > w2:
            s = 1
            w2 = w1
        elif w1 == w2:
            s += 1
print(s,w2)