# 입력 처리
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최소 최대값
minVal = 1e9
maxVal = -1e9

def dfs(i, cur):
  global maxVal, minVal, add, sub, mul, div
  if i == n:
    minVal = min(minVal, cur)
    maxVal = max(maxVal, cur)
  else:
    if add > 0:
      add -= 1
      dfs(i + 1, cur + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, cur - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, cur * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, int(cur / data[i]))
      div += 1

dfs(1, data[0])

print(maxVal)
print(minVal)
