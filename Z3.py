import math
def points_in_circle(points, r=1):
    count = 0
    for x, y in points:
        if math.sqrt(x**2 + y**2) <= r:
            count += 1
    l=[r,count]       
    return l