n = int(input())
m = int(input())
i = 1
way = [1]
while i != 0:
    if (i + m - 1) % n != 0:
        i = (i + m - 1) % n
    else:
        i = n
    if i == 1:
        break
    way.append(i)
for j in way:
    print(j, end='')
