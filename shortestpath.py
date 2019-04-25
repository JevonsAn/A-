from queue import PriorityQueue
from math import sqrt
import time


def getgraph(filename):
    graph = []
    src = (8, 4)
    dst = (10, 14)
    with open(filename) as f:
        x = 0
        for line in f.readlines():
            newline = []
            y = 0
            for word in line.strip().split(" "):
                if word == "s":
                    src = (x, y)
                    newline.append(0)
                elif word == "t":
                    dst = (x, y)
                    newline.append(0)
                else:
                    newline.append(int(word))
                y += 1
            x += 1

            graph.append(newline)

    height = len(graph)
    width = len(graph[0])
    return graph, height, width, src, dst


def findpath(graph, height, width, src, dst):
    print("开始A*算法")
    start_time = time.process_time()
    best_queue = PriorityQueue()
    visited = [[0] * width for i in range(height)]

    def hn(dot):
        return sqrt((dot[0] - dst[0]) ** 2 + (dot[1] - dst[1]) ** 2)

    best_queue.put((0, 0, src, [src]))
    ci = 0
    endpath = []
    while True:
        ci += 1
        # if ci > 50:
        #     break
        f, g, now, path = best_queue.get()
        # print(path)
        x, y = now

        # 终止条件
        if now == dst:
            print(path)
            print(g)
            print(ci)
            endpath = path
            break

        # 是否访问过

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < height and 0 <= j < width and (i != x or j != y) and graph[i][j] >= 0:
                    # print((i, j), newh)
                    if i == x or j == y:
                        newg = g + 1 + graph[i][j]
                        # if visited[i][j]:
                        #     continue
                        # visited[i][j] = 1
                        # newh = hn((i, j))
                        if visited[i][j]:
                            if newg > visited[i][j][0]:
                                continue
                            newh = visited[i][j][1]
                            visited[i][j][0] = newg
                        else:
                            newh = hn((i, j))
                            visited[i][j] = [newg, newh]
                        newpath = path + [(i, j)]
                        best_queue.put((newg + newh, newg, (i, j), newpath))
                    else:
                        newg = g + sqrt(2) + graph[i][j]
                        # if visited[i][j]:
                        #     continue
                        # visited[i][j] = 1
                        # newh = hn((i, j))
                        if visited[i][j]:
                            if newg > visited[i][j][0]:
                                continue
                            newh = visited[i][j][1]
                            visited[i][j][0] = newg
                        else:
                            newh = hn((i, j))
                            visited[i][j] = [newg, newh]
                        newpath = path + [(i, j)]
                        best_queue.put((newg + newh, newg, (i, j), newpath))

    print("运行时间：", (time.process_time() - start_time) * 1000, "ms")
    for dot in endpath:
        graph[dot[0]][dot[1]] = "x"

    for i in range(height):
        for j in range(width):
            print(graph[i][j], end=" ")
        print()

    return endpath, (time.process_time() - start_time)


def generateGraph2():
    graph = [[0] * 40 for i in range(20)]
    i = 2
    for j in range(0, 13):
        if j not in (7, 11):
            graph[i][j] = -1
    i = 6
    for j in range(2, 8):
        graph[i][j] = -1

    i = 15
    for j in range(4, 9):
        graph[i][j] = -1

    j = 12
    for i in range(0, 8):
        graph[i][j] = -1
    for i in range(12, 20):
        graph[i][j] = -1

    j = 3
    for i in [0] + list(range(11, 20)):
        if i != 17:
            graph[i][j] = -1

    j = 7
    for i in [0, 1, 5, 7, 9, 10, 17, 18, 19]:
        graph[i][j] = -1

    j = 8
    for i in [3, 5, 10, 11, 12, 13, 14]:
        graph[i][j] = -1

    j = 5
    for i in range(7, 12):
        graph[i][j] = -1

    j = 2
    for i in (7, 10, 11):
        graph[i][j] = -1

    graph[13][9] = -1
    graph[13][11] = -1
    graph[11][4] = -1

    for i in range(10, 13):
        for j in range(19, 22):
            graph[i][j] = -1

    for i in range(15, 17):
        for j in range(24, 26):
            graph[i][j] = -1

    graph[10][28] = -1
    graph[11][31] = -1
    graph[13][31] = -1
    graph[9][36] = -1
    graph[7][36] = -1

    i = 0
    for j in range(24, 40):
        graph[i][j] = 4
    i = 1
    for j in range(25, 40):
        graph[i][j] = 4
    i = 2
    for j in range(26, 40):
        graph[i][j] = 4
    i = 3
    for j in range(26, 37):
        graph[i][j] = 4
    i = 4
    for j in range(26, 36):
        graph[i][j] = 4
    i = 5
    for j in range(27, 33):
        graph[i][j] = 4
    i = 6
    for j in range(27, 33):
        graph[i][j] = 4
    i = 7
    for j in range(29, 33):
        graph[i][j] = 4

    x = 34
    for i in range(1, 4):
        graph[i][x] = 2
        x -= 1

    j = 32
    for i in range(8, 20 - 2):
        graph[i][j] = 2

    j = 33
    for i in range(4, 20 - 3):
        graph[i][j] = 2

    j = 34
    for i in range(5, 20 - 5):
        graph[i][j] = 2

    j = 35
    for i in range(7, 12):
        graph[i][j] = 2

    x = 31
    for i in range(16, 20):
        for j in range(x, x + 3):
            graph[i][j] = 2
        x -= 1

    x = 35
    for i in range(9, 13):
        graph[i][x] = 0
        x -= 1

    graph[15][31] = 2
    graph[10][36] = 2

    graph[10][4] = "s"
    graph[0][35] = "t"
    with open("static/graphs/graph2.txt", "w") as f:
        for line in graph:
            for w in line:
                f.write(str(w) + " ")
            f.write("\n")


if __name__ == '__main__':
    # generateGraph2()
    findpath(*getgraph("static/graphs/graph1.txt"))
    findpath(*getgraph("static/graphs/graph2.txt"))
