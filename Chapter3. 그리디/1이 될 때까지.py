n, k = map(int, input().split())
''' 내 풀이 '''
# count = 0
# while n != 1:
#     if n%k == 0:
#         n = n//k
#         count += 1
#     else:
#         n = n -1
#         count += 1
# print(count)

''' 정답 '''
result = 0
while True:
    target = (n//k)*k
    result += n - target
    n = target

    if n < k :
        break
    
    result += 1
    n = n // k

result += n-1
print(result)

# N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도
# 빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로
# 한 번에 빼는 방식으로 소스코드를 작성해야 한다.

# N이 커졌을 때도 효율적으로 코드가 돌아가도록
# 사고하는 생각을 길러야 겠다.
