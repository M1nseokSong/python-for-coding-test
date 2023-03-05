import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
n = int(input())
shop_array = list(map(int, input().split()))
m = int(input())
customer_array = list(map(int, input().split()))
shop_array.sort()
for _ in customer_array:
    result = binary_search(shop_array, _, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
