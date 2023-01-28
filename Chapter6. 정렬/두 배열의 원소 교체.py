n, k = map(int, input().split())
# a = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for _ in range(k):
    if a[_] < b[_]:
        a[_], b[_] = b[_], a[_]
    else:
        break

print(sum(a))
