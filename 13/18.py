# 구현
# 요구사항에 따른 재귀함수 작성

def getBalancedIndex(p):
  count = 0 # 여는 괄호 개수
  for i in range(len(p)):
    if p[i] == '(':
      count += 1
    else:
      count -= 1
    if count == 0:
      return i

def isProper(p):
  count = 0 # 여는 괄호 개수
  for i in p:
    if i == '(':
      count += 1
    else:
      if count == 0:
        return False
      count -= 1
  return False

def solution(p):
  answer = ''
  if p == '':
    return answer
  balancedIndex = getBalancedIndex(p)
  u = p[:balancedIndex + 1]
  v = p[balancedIndex + 1:]
  if isProper(p):
    answer = u + solution(v)
  else:
    answer = '('
    answer += solution(v)
    answer += ')'
    u = list(u[1:-1]) # 리스트 변환 -> 문자열 분리 -> 순회
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')'
      else:
        u[i] = '('
    answer += "".join(u) # 문자열 병합
  return answer
