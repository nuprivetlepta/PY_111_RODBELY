import random as rnd


def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot_index = len(lst) // 2
        pivot_value = lst[pivot_index]
        malishi = [i for i in lst if i < pivot_value]
        pivotiki = [i for i in lst if i == pivot_value]
        bolshi = [i for i in lst if i > pivot_value]
        return [quicksort(malishi) + pivotiki + quicksort(bolshi)]


def selection(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def merg_fn(left_side: list[int], right_side: list[int]):

    sorted_res = []
    cur_l_ind = 0
    cur_r_ind = 0

    while True:
        cur_l_val = left_side[cur_l_ind]
        cur_r_val = right_side[cur_r_ind]

        if cur_l_val < cur_r_val:
            sorted_res.append(cur_l_val)
            cur_l_ind += 1
        else:
            sorted_res.append(cur_r_val)
            cur_r_ind += 1

        if cur_l_ind == len(left_side):
            sorted_res.extend(right_side[cur_r_ind:])
            break

        elif cur_r_ind == len(left_side):
            sorted_res.extend(left_side[cur_l_ind:])
            break


def merge(lst):
    if len(lst) == 1:
        return lst

    mid_ind = len(lst) // 2
    ar_1 = merge(lst[: mid_ind])
    ar_2 = merge(lst[mid_ind:])
    return merg_fn(ar_1, ar_2)


if __name__ == '__main__':
    lafa = [rnd.randint(13, 26) for i in range(10**6)]
    print(quicksort(lafa))
    # print(merge(lafa))
    print(selection(lafa))

