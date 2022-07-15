from tarfile import LENGTH_NAME


n = int(input())
array = list(map(int, input().split()))
i = 0
for ele in range(1, n) :
    if array[ele] < array[ele - 1] :
        i = i + array[ele - 1] - array[ele]
        array[ele] = array[ele - 1]
print(i)

