unsorted = [1.2, 0.22, 0.43, 0.36, 0.39, 0.27]


def bucket_sort(arr):
    size = len(arr)
    biggest = max(arr)
    buckets = [[]] * size

    for i in range(len(unsorted)):
        j = int(arr[i] / size)
        print(f"{j=}")
        if j != len(arr):

            print("buckets[j].append(arr[i])")
            buckets[j].append(arr[i])
        else:
            print("buckets[len(arr) - 1].append(arr[i])")
            buckets[len(arr) - 1].append(arr[i])
        print(buckets)


max, min = max(unsorted), min(unsorted)
rnge = (max - min)
no_buckets = range(max - min) /
bucket_sort(unsorted)