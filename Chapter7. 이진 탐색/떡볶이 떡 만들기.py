import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

max_array = max(array)

def binary_search(array, start, end):
    while start <= end:
        total = 0
        mid = (start+end)//2
        for x in array:
            if x > mid:
                total += (x-mid)
        if total < m:
            end = mid -1
        elif total > m:
            start = mid + 1
        else:
            return mid
print(binary_search(array, 0, max_array))
