n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# 5 8 3
# 2 4 5 4 6 -> 6 6 6 5 6 6 6 5 = 46

# 5 13 3
# 2 4 5 4 6 -> 6 6 6 5 6 6 6 5 6 6 6 5 6
# 이론상 제일 큰수 k번, 그 다음 큰수 1번을 한 세트로 보고 반복하면 됨.
array.sort(reverse=True)
repeat = m // (k+1)
remain = m % (k+1) 
result = (array[0]*k + array[1]) * repeat + (array[0] * remain)

print(result)

# 가장 큰수 k번, 그 다음 큰수 1번을 한 세트로 묶는다는 생각을 처음에 못함.
