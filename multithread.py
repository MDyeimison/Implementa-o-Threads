import threading
import random
import time

def random_numbers_generator(num_random_numbers = 30000):
    list_rand = []
    with open("random_numbers.txt", "w") as f:
        for i in range(num_random_numbers):
            random_num = random.randint(1, 1000)
            f.write(str(random_num) + "\n")
        f.close()

    with open("random_numbers.txt", "r") as f:
        for e in f:
            for word in e.split():
                list_rand.append(int(word))
        f.close()
    return list_rand
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def heapsort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == '__main__':
    arr = random_numbers_generator()
    arr2 = arr[:]
    arr3 = arr[:]

    print(f'Valores originais (10 primeiros valores): {arr[:10]}')

    start_time = time.time()

    t1_start_time = time.time()
    t1 = threading.Thread(target=bubble_sort(arr))
    t1.start()

    t2_start_time = time.time()
    t2 = threading.Thread(target=heapsort(arr2))
    t2.start()

    t3_start_time = time.time()
    t3 = threading.Thread(target=shell_sort(arr3))
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    t1_end_time = time.time()
    t2_end_time = time.time()
    t3_end_time = time.time()

    end_time = time.time()

    print("Thread 1 levou %0.2f segundos" % (t1_end_time - t1_start_time))
    print(f'Bubble Sort: {arr[:10]}')
    print("Thread 2 levou %0.2f segundos" % (t2_end_time - t2_start_time))
    print(f'Heapsort{arr2[:10]}')
    print("Thread 3 levou %0.2f segundos" % (t3_end_time - t3_start_time))
    print(f'Shell sort: {arr3[:10]}')