n = int(input())
data = list(map(int, input().split()))
data.sort()  # 오름차순

result = 0  # 총 그룹 수
count = 0  # target 그룹의 모험가 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
