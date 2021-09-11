circle = open('file1.txt', 'r')
point_file = open('file2.txt', 'r')
centre = tuple(map(float, circle.readline().split()))
rad = float(circle.readline())
point = point_file.readlines()
print(point)
points = []
for i in point:
    points.append(list(map(float, i.strip().split())))
print(points)
for j in points:
    pos = (j[0] - centre[0])**2 + (j[1] - centre[1])**2
    if pos < rad**2:
        print(1, end='\n')
    elif pos > rad**2:
        print(2, end='\n')
    elif pos == rad**2:
        print(0, end='\n')
