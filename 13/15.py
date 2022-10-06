# 모든 간선의 비용이 동일 -> BFS
# O(N + M) -> ~2천만 OK

from collections import deque

# 입력 처리
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# print(n, m, k, x)

# 도로 정보 저장
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시

# BFS
def bfs(graph, start, visited, distance):
  visited[start] = True
  queue = deque([start])
  while queue:
    vertex = queue.popleft()
    for i in graph[vertex]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        distance[i] = distance[vertex] + 1 # target

visited = [False] * (n + 1)
bfs(graph, x, visited, distance)

# 출력 처리
isFound = False
for i in range(1, n + 1):
  if distance[i] == k:
    isFound = True
    print(i)

if not isFound:
  print(-1)
