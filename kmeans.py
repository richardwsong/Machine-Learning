import sys; args = sys.argv[1:]
import random
import math
from PIL import Image


def euclidean(one, two):
    return (one[0]-two[0])**2 + (one[1]-two[1])**2 + (one[2]-two[2])**2


file = args[1]
k = int(args[0])

# file = "cat.jpg"
# k = 20

im = Image.open(file)
px = im.load()

width, height = im.size

means = []
grid = []
sameVal = []
points = []
uniquePoints = dict()

for h in range(height):
    for w in range(width):
        if px[w, h] not in uniquePoints:
            uniquePoints[px[w, h]] = 1
        else:
            uniquePoints[px[w, h]] += 1

def average(val):
    a = 0
    b = 0
    c = 0
    length = 0
    for i in val:
        for k in range(uniquePoints[(i[0], i[1], i[2])]):
            a += i[0]
            b += i[1]
            c += i[2]
            length+=1
    return int(a/length), int(b/length), int(c/length)


def average2(val):
    a = 0
    b = 0
    c = 0
    length = 0
    for i in val:
        for k in range(uniquePoints[(i[0], i[1], i[2])]):
            a += i[0]
            b += i[1]
            c += i[2]
            length += 1
    return (a / length), (b / length), (c / length)

def average3(val):
    length = 0
    for i in val:
        for k in range(uniquePoints[(i[0], i[1], i[2])]):
            length += 1
    return length

maxVal = 0
maxTuple = ()

for i in uniquePoints:
    if uniquePoints[i] > maxVal:
        maxVal = uniquePoints[i]
        maxTuple = i

for i in range(k):
    h = random.randint(0, height-1)
    w = random.randint(0, width-1)
    means.append(px[w, h])
    points.append(set())


for h in range(0, height):
    grid.append([])
    sameVal.append([])
    for w in range(0, width):
        grid[h].append(random.randint(0, k-1))
        sameVal[h].append(0)

regionNum = []
for i in range(k):
    regionNum.append(0)

tupleToMean = dict()

def kmeans():
    # print("start")
    # sum = math.inf
    # val = math.inf
    visited = set()
    while True:
        changes = [0] * k
        visited.clear()
        # sum = 0
        old = means.copy()
        for h in range(0, height):
            for w in range(0, width):
                if px[w, h] in visited:
                    grid[h][w] = tupleToMean[px[w, h]]
                    continue
                visited.add(px[w,h])
                if sameVal[h][w] >= 20:
                    continue
                pixel = px[w, h]
                minDist = math.inf
                minMean = -1
                for m in range(0, k):
                    dist = euclidean(pixel, means[m])
                    if dist < minDist:
                        minDist = dist
                        minMean = m
                if grid[h][w] == minMean:
                    sameVal[h][w] += 1
                else:
                    sameVal[h][w] = 0
                    changes[minMean] += 1
                grid[h][w] = minMean
                points[minMean].add(px[w, h])
                if px[w,h] in tupleToMean and tupleToMean[px[w,h]] != minMean and px[w,h] in points[tupleToMean[px[w,h]]]:
                    points[tupleToMean[px[w,h]]].remove(px[w,h])
                tupleToMean[px[w, h]] = minMean

        for i in range(0, k):
            if len(points[i]) != 0:
                avg = average2(points[i])
                means[i] = avg
                # sum += (euclidean(old[i], means[i]))
            else:
                means[i] = old[i]
        # val = sum
        # print(changes)
        if sum(changes) == 0:
            break

visit = set()

def bfs(coord):
    q = list()
    q.append(coord)
    while len(q) != 0:
        temp = q.pop(0)
        if temp in visit:
            continue
        visit.add(temp)
        h = temp[0]
        w = temp[1]
        if h + 1 < height and w - 1 >= 0 and grid[h + 1][w - 1] == grid[h][w]:
           q.append((h + 1, w - 1))
        if h+1 < height and grid[h+1][w] == grid[h][w]:
           q.append((h + 1, w))
        if h+1 < height and w+1 < width and grid[h+1][w+1] == grid[h][w]:
           q.append((h + 1, w + 1))
        if w+1 < width and grid[h][w+1] == grid[h][w]:
           q.append((h, w + 1))
        if w - 1 >= 0 and grid[h][w - 1] == grid[h][w]:
           q.append((h, w - 1))
        if h-1 >= 0 and w-1 >= 0 and grid[h-1][w-1] == grid[h][w]:
           q.append((h-1, w-1))
        if h - 1 >= 0 and grid[h - 1][w] == grid[h][w]:
           q.append((h - 1, w))
        if h-1 >= 0 and w+1 < width and grid[h-1][w+1] == grid[h][w]:
           q.append((h-1, w+1))

def floodFill():
    for h in range(height):
        for w in range(width):
            if (h, w) not in visit:
                regionNum[grid[h][w]] += 1
                bfs((h, w))

dic = []

print("Size:", width, "x", height)
print("Pixels:", width*height)
print("Distinct pixel count:", len(uniquePoints))
print("Most common pixel:", maxTuple, "=>", maxVal)
print("Final means:")
kmeans()

avSum = 0

for i in range(k):
    tup = average2(points[i])
    tup2 = average(points[i])
    length = average3(points[i])
    num = str(i+1) + ":"
    print(num, tup, "=>", length)
    avSum+=length
    # print(num, tup)
    dic.append(tup2)
# print(avSum)

floodFill()

#
print("Region Counts:", end=" ")
for i in range(k):
    if i != k-1:
        print(regionNum[i], end=", ")
    else:
        print(regionNum[i])
for h in range(height):
    for w in range(width):
        px[w, h] = dic[grid[h][w]]

# im.save("kmeans/{}.png".format("2021rsong"), "PNG")
im.save("new_image.png")