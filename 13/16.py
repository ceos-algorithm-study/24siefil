# 전체 맵 크기: 8 x 8
# 벽을 설치할 수 있는 모든 케이스의 개수: 64C3 = 44664 < 백만 -> 완전탐색
# 조합 -> DFS/BFS
# 1. DFS 활용 벽 설치
# 2. DFS 활용 각 케이스에 대해 바이러스 전파
# 3. 최대값 갱신

# 입력 처리
n, m = map(int, input().split())
data = [] # 초기 맵
for _ in range(n):
  data.append(list(map(int, input().split())))
temp = [[0] * m for _ in range(n)] # 벽 설치 이후 바이러스를 전파시킬 맵

# 방향 백터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def spreadVirus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >=0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        spreadVirus(nx, ny)

def getSafeCount():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# DFS: 울타리를 설치하며 매번 안전 영역의 크기를 계산
def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

      # 바이러스 전파
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          spreadVirus(i, j)
    result = max(result, getSafeCount())
    return

  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
