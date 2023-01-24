# 내 풀이 : move_types를 굳이 type를 in으로  for문을 돌려 count 라는 변수를 하나 더 쓰게 됨.
# 정답 코드에서는 in range로 for문을 돌려 count라는 변수는 필요 없음. 다만 tmp_x, tmp_y라는 새로운 변수는 필요함.
# 비슷한 듯 하지만 코드의 간결성은 정답 코드가 더 좋아보임.

# n = int(input())
# move = list(input().split()) # ['R', 'R', 'R', 'U', 'D', 'D]
# start_x = 1; start_y = 1
# wall = [0, 6]
# move_types = ['L', 'R', 'U', 'D']
#             #  0    1    2    3    count
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for turn in move:
#     count = 0
#     for type in move_types:
#         if turn != type:
#             count += 1
#         else:
#             break

#     if ((start_x + dx[count]) in wall) or ((start_y + dy[count]) in wall):
#         continue
#     else:
#         start_x += dx[count]
#         start_y += dy[count]

# print(start_x, start_y)

# 정답 코드
n = int(input())
move = list(input().split()) # ['R', 'R', 'R', 'U', 'D', 'D]
start_x = 1; start_y = 1
wall = [0, 6]
move_types = ['L', 'R', 'U', 'D']
            #  0    1    2    3    count
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for turn in move:
    for type in range(len(move_types)):
        if turn == move_types[type]:
            tmp_x = start_x + dx[type]
            tmp_y = start_y + dy[type]
    if (tmp_x in wall) or (tmp_y in wall):
        continue
    else:
        start_x = tmp_x
        start_y = tmp_y

print(start_x, start_y)
