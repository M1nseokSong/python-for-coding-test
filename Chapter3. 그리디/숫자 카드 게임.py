n, m = map(int, input().split())

# 2차원 배열 리스트 입력받는 방법
card = list(list(map(int, input().split())) for _ in range(n))

min_card = list()

for _ in range(n):
    min_card.append(min(card[_]))

print(max(min_card))

# 2차원 배열 리스트를 입력을 처음부터 받아도 되고
# 한 줄 씩 입력받아 확인 하는 방법도 있다.
# 현재 줄에서 '가장 작은 수'를 찾고
# '가장 작은 수'들 중에서 가장 큰 수를 계속 해서 update 하는 방식.
