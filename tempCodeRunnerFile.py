n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

sortArr = sorted(arr)
print(sortArr[-1], sortArr[-2], sep='\n')