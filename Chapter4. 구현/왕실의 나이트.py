# 상하좌우.py와 유사함.
# move_track_r, move_track_c 대신 [(-2, -1), (-1, -2) ,,, ,(-2, 1)] 으로 하나의 리스트로 방향을 정의할 수도 있음.
# 두 가지 방법 다 알고 있자.

n = input()
count = 0
row, column = int(n[1]), ord(n[0])-96 # a, b, c  -> 1, 2, 3
move_track_r = [-2, -2, -1, -1, 1, 1, 2, 2]
move_track_c = [1, -1, 2, -2, 2, -2, 1, -1]
for chance in range(8):
    dx = row + move_track_r[chance]
    dy = column + move_track_c[chance]
    if dx <= 0 or dx >= 9 or dy <= 0 or dy >= 9:
        pass
    else:
        count += 1
print(count)
