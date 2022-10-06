def rotateMatrixBy90Degree(matrix):
  n = len(matrix) # 행 길이
  m = len(matrix) # 열 길이
  result = [[0] * n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n - i - 1] = a[i][j]

  return result

def checkAll1(newLock):
  lockLength = len(newLock) //3
  for i in range(lockLength, lockLength * 2):
    for j in range(lockLength, lockLength * 2):
      if newLock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)

  # 자물쇠의 크기를 기존의 3배로 변환
  newLock = [[0] * (n * 3) for _ in range(n * 3)]
  # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
  for i in range(n):
    for j in range(n):
      newLock [i + n][j + n] = lock[i][j]

  # 4가지 방향에 대해 확인
  for rotation in range(4):
    key = rotateMatrixBy90Degree(key)
    for x in range(n * 2):
      for y in range(n * 2):
        for i in range(m):
          for j in range(m):
            newLock[x + i][y + j] += key[i][j]
        if checkAll1(newLock) == True:
          return True
        for i in range(m):
          for j in range(m):
            newLock[x + i][y + j] -= key[i][j]
  return False
