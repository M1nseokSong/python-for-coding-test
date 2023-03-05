import sys
input = sys.stdin.readline
N = int(input())
food = list(map(int, input().split()))
dp_table = [0] * N
dp_table[0] = food[0]
dp_table[1] = max(dp_table[0], food[1])
for i in range(2, N):
    dp_table[i] = max(dp_table[i-2]+food[i], dp_table[i-1])
print(dp_table[N-1])
