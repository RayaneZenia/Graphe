import time
import random
import matplotlib.pyplot as plt

def tri_par_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        e = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > e:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = e

def tri_par_fusion(arr):
    def fusion(debut, milieu, fin):
        n1 = milieu - debut + 1
        n2 = fin - milieu
        G = arr[debut: milieu + 1]
        D = arr[milieu + 1: fin + 1]
        i = j = 0
        k = debut
        while i < n1 and j < n2:
            if G[i] <= D[j]:
                arr[k] = G[i]
                i += 1
            else:
                arr[k] = D[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = G[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = D[j]
            j += 1
            k += 1

    def tri(debut, fin):
        if debut < fin:
            milieu = (debut + fin) // 2
            tri(debut, milieu)
            tri(milieu + 1, fin)
            fusion(debut, milieu, fin)

    tri(0, len(arr) - 1)

def tri_par_denombrement(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    k = 0
    for i in range(len(count)):
        for _ in range(count[i]):
            arr[k] = i
            k += 1

def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_time(algorithm, lst):
    start_time = time.time()
    algorithm(lst)
    end_time = time.time()
    return end_time - start_time

sizes = [100, 200, 300, 400, 500]
insertion_sort_times = []
merge_sort_times = []
counting_sort_times = []

for size in sizes:
    lst = generate_random_list(size)
    insertion_sort_times.append(measure_time(tri_par_insertion, lst.copy()))
    merge_sort_times.append(measure_time(tri_par_fusion, lst.copy()))
    counting_sort_times.append(measure_time(tri_par_denombrement, lst.copy()))

plt.plot(sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(sizes, merge_sort_times, label='Merge Sort')
plt.plot(sizes, counting_sort_times, label='Counting Sort')
plt.xlabel('Size of List')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.show()
