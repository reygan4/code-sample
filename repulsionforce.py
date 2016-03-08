p = [map(float,raw_input().split(" ")) for i in range(2)]
print  p[0][0]*p[1][0] /((p[0][1] - p[1][1]) ** 2 + (p[0][2]-p[1][2])**2)
