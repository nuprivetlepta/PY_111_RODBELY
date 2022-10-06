def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        malishi = [i for i in lst[1:] if i <= pivot]
        bolshi = [i for i in lst[1:] if i > pivot]
        return quicksort(malishi) + [pivot] + quicksort(bolshi)


def selection(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def merge(lst):
    if len(lst) == 1:
        return lst
    else:
        ar_1 = lst[:len(lst)//2]
        ar_2 = lst[len(lst)//2:]


if __name__ == '__main__':
    l = [1, 4, 11, 6546, 32, 566, 11, 6546, 987, 11, 645, 0, 87]
    print(selection(l))

