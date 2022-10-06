def leng(n: list):
    count = 0


def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        malishi = [i for i in lst[1:] if i <= pivot]
        bolshi = [i for i in lst[1:] if i > pivot]
        return quicksort(malishi) + [pivot] + quicksort(bolshi)


def rental_reverse(ords: list) -> bool:
    flag = True
    orders = quicksort(ords)
    for numb in range(1, len(orders)-1):
        if orders[numb][0] < orders[numb-1][1]:
            flag = False
            return flag
    return flag


def rental_str(ords: list) -> bool:
    flag = True
    orders = quicksort(ords)
    for numb in range(len(orders)-2):
        if orders[numb][1] > orders[numb+1][0]:
            flag = False
            return flag
    return flag



if __name__ == '__main__':
    queue = [[1, 2], [5, 10], [8, 22], [11, 23]]
    print(rental_reverse(queue))
    print(rental_str(queue))


