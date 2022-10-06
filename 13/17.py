# 200 * 200 < 백만 -> 완전 탐색, 2차원 좌표 -> 그래프 탐색
# 순차적으로 깊이 증가 -> 너비 우선 탐색 -> BFS -> Queue 활용 (deque 사용)

from collections import deque

n, k = map(int, input().split())

graph = []
data = [] # 바이러스에 대한 정보

# 입력 처리
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j)) # tuple
data.sort()

targetS, targetX, targetY = map(int, input().split())

# 방향 백터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque(data) # 초기화된 큐
while queue:
  virus, s, x, y = queue.popleft()
  if s == targetS:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        queue.append((virus, s + 1, nx, ny))

# 출력 처리
print(graph[targetX - 1][targetY -1])
