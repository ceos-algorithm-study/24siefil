data = input()

result = int(data[0])

for i in range(1, len(data)):
  temp = int(data[i])
  if temp <= 1 or result <= 1:
    result += temp
  else:
    result *= temp

print(result)
