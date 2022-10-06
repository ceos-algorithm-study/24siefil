n = input()
totalLength = len(n)

leftSum = 0
rightSum = 0

# left part
for i in range(totalLength // 2):
  leftSum += int(n[i])

# right part
for i in range(totalLength // 2, totalLength):
  rightSum += int(n[i])

if leftSum == rightSum:
  print('LUCKY')
else:
  print('READY')
