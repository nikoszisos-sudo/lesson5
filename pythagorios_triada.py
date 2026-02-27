for a in range(1, 21, 1):
    for b in range(1, 21, 1):
        for c in range(1, 21, 1):
            if a*a + b*b == c*c:
                print(str(a) + "," + str(b) + "," + str(c))
