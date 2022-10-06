def game(n: int, k: int):
    gamers = [i for i in range(n)]
    slogi = k
    while len(gamers) > 1:
        if slogi > len(gamers):
            off_boy = (slogi % len(gamers)) - 1
        else:
            off_boy = slogi - 1
        gamers.pop(off_boy)
        gamers = gamers[off_boy:] + gamers[:off_boy]
    return gamers[0]


# def navi(start: (int, int), stop: (int, int)) -> int:
#     our_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     total_cost = 0
#
#     if start == stop:
#         total_cost += our_field[start[0]][start[1]]
#         return total_cost


if __name__ == '__main__':
    #проверка считалки
    people_count = 5
    slogi = 3
    print(game(people_count, slogi))

