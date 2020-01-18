# 幅優先探索（BFS)
def calc_maze(maze, sh, sw):
    H = len(maze)
    W = len(maze[0])

    # 距離行列
    distance = []
    for i in range(H):
        distance.append([])
        for j in range(W):
            distance[i].append(-1)

    # 座標格納キュー
    # (H座標, W座標, 距離)
    queue = []
    # 初期ポジション格納
    queue.append((sh, sw))
    distance[sh][sw] = 0
    # 最大距離を格納
    max_distance = 0
    # 探索する場所がなくなるまで
    while queue:
        h, w = queue.pop(0)

        for i in range(0, 4):
            nh, nw = h + [1, 0, -1, 0][i], w + [0, 1, 0, -1][i]
            if (0 <= nh and nh < H and 0 <= nw and nw < W and maze[nh][nw] != '#' and distance[nh][nw] == -1):
                queue.append((nh, nw))
                distance[nh][nw] = distance[h][w] + 1
                # 最大距離更新
                if max_distance < (distance[h][w] + 1):
                    max_distance = distance[h][w] + 1
    return max(max(d) for d in distance)



def main():
    H, W = map(int, input().split())
    maze = []
    ans = 0

    for _ in range(H):
        l = list(input())
        maze.append(l)

    for j in range(W):
        for i in range(H):
            if maze[i][j] != "#":
                ans = max(ans, calc_maze(maze, i, j))
    print(ans)
    return 0
if __name__ == '__main__':
    main()
