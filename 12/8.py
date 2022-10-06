data = input()
result = []
numberSum = 0

for i in data:
  if i.isalpha():
    result.append(i)
  else:
    numberSum += int(i)

result.sort()

result.append(str(numberSum))

print(''.join(result)) # list to str

# https://velog.io/@aonee/Python-list%EB%A5%BC-%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C-.join%EB%A6%AC%EC%8A%A4%ED%8A%B8
# https://wayhome25.github.io/python/2017/02/26/py-14-list/
