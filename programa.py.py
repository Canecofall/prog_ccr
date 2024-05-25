b = 0
a = 0
a, b = map(float, input().split(" "))
if a == 0.00 and b == 0.00:
    print("0.00%")
else:
    c = b - a
    d = c / a
    print(f"{d*100:.2f}%")