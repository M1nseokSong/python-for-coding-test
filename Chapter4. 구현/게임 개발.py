# 0은 육지, 1은 바다, 2는 내가 간 곳
# 바다와 간 곳을 구별 하지 않고 간 곳도 바다로 바꾸는 코드를 하니 정답이 틀렸음.
# 주어진 조건을 제대로 읽고 그대로 구현하는 사고가 필요하다.
# 정답 코드와는 생각한 방법이 다르다.

n, m = map(int, input().split())
char_x, char_y, look = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
change_look = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 지금 바라보는 방향 북, 서, 남, 동 기준으로 그 다음 갈 방향
change_back = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 지금 바라보는 방향 북, 서, 남, 동 기준으로 뒤로 가는 방향
if look == 1:
    look = 3
if look == 3:
    look = 1
tmp_look = [0, 1, 2, 3] * 10000
count = 1
map[char_x][char_y] = 2

while True:
    for turn in range(4):
        if map[char_x + change_look[tmp_look[look]][0]][char_y + change_look[tmp_look[look]][1]] != 0:
            look += 1
        elif map[char_x + change_look[tmp_look[look]][0]][char_y + change_look[tmp_look[look]][1]] == 0:
            char_x += change_look[tmp_look[look]][0]
            char_y += change_look[tmp_look[look]][1]
            count += 1
            look += 1
            map[char_x][char_y] = 2
            break

    else:
        dx = char_x + change_back[tmp_look[look]][0]
        dy = char_y + change_back[tmp_look[look]][1]
        if map[dx][dy] == 1:
            break
        else:
            char_x = dx
            char_y = dy
            map[char_x][char_y] = 2
            if map[char_x][char_y] == 0:
                count += 1

print(map)
print(count)
