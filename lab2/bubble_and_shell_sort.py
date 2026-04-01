import random
import time


def bubble_sort(mylist):
    last_item = len(mylist) - 1
    copy_counter = 0
    comparison_counter = 0

    for z in range(last_item):
        for x in range(last_item - z):
            copy_counter += 1
            comparison_counter += 1
            if mylist[x] > mylist[x + 1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]

    print("copy counter:", copy_counter, "comparison counter:", comparison_counter)
    return mylist


def shellsort(l):
    copy_counter = 0
    comparison_counter = 0
    h = 1
    n = len(l)

    while h < n // 3:
        h = 3 * h + 1

    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h:
                comparison_counter += 1
                if l[j - h] > l[j]:
                    l[j - h], l[j] = l[j], l[j - h]
                    copy_counter += 1
                    j -= h
                else:
                    break
        h //= 3

    print("copy counter:", copy_counter, "comparison counter:", comparison_counter)
    return l


def main():
    print("Bubble Sort")
    old_list = random.sample(range(0, 100), 100)
    print("Old List:", old_list)
    t1 = time.perf_counter()
    new_list = bubble_sort(old_list)
    t2 = time.perf_counter()
    print("Time:", t2 - t1)
    print("New List:", new_list)

    print()
    print("Shell Sort")
    unsorted_list = random.sample(range(0, 10000), 10000)
    print("Unsorted:", unsorted_list)
    t1 = time.perf_counter()
    sorted_list = shellsort(unsorted_list)
    t2 = time.perf_counter()
    print("Time:", t2 - t1)
    print("Shell sorted:", sorted_list)


if __name__ == "__main__":
    main()
