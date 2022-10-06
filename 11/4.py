n = input()
data = list(map(int, input().split()))
data.sort()

target = 1 # result
for i in data:
  if target < i:
    break
  else:
    target += i

print(target)

