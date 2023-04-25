def counting_sort(arr):
    max_val = max(arr) + 1
    count = [0] * max_val

    for num in arr:
        count[num] += 1

    for i in range(1, max_val):
        count[i] += count[i-1]

    output = [0] * len(arr)

    for num in arr:
        output[count[num]-1] = num
        count[num] -= 1

    return output

arr = [1,5,2,5,3,6,7,4,8,1,0,2]
counting_sort(arr)
print(arr)