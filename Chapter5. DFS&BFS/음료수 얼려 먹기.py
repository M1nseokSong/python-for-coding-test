# DFS를 처음 접해봐서 아이디어 떠올리는데 어려웠다.
# 입력 값을 받을 때 세로 길이 n은 행이고, 가로 길이 m은 열이다.
# DFS는 스택 자료구조를 이용한 재귀를 쓰기 때문에, 내가 맨 처음 넣었던 예를 들어 (0, 0) 그 다음 쭉 return True를 하더라도
# dfs(0, 0)으로는 마지막 (0, 0)의 True만 결과 값으로 나온다.
# 재귀함수는 return을 어떻게 잡아주느냐가 관건인 것 같다.

n, m = map(int, input().split()) # n행 m열
ice_box = [list(map(int, input())) for _ in range(n)]
# ice_coor = [list((row, col) for col in range(n)) for row in range(m)]
count = 0
def dfs(ice_box, row, col):
    if row <= -1 or row >= n or col <= -1 or col >= m:     
        return False
    if ice_box[row][col] == 0:
        ice_box[row][col] = 2
        dfs(ice_box, row+1, col)
        dfs(ice_box, row-1, col)
        dfs(ice_box, row, col+1)
        dfs(ice_box, row, col-1)
        #print(row, col)
        return True
    return False

for row in range(n):
    for col in range(m):
        #if ice_box[row][col]==0:    # 실행시간이 단축될 거 같은데,,,
            if dfs(ice_box, row, col) == True:
                count += 1
print(count)
