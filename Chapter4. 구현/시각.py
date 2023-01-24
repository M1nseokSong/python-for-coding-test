# 완전 탐색유형으로 분류 : 가능한 경우의 수를 모두 검사해보는 탐색 방법
# 비효울적인 시간 복잡도를 가지고 있으므로 데이터 개수가 큰 경우 정상적으로 동작 안할 수 있음.
# 따라서 전체 확인(탐색)해야 할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 적절함.

n = int(input())
count = 0
for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if "3" in str(h)+str(m)+str(s):
                count += 1
print(count)
