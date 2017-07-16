def square_of_sum(num):
    return sum(range(1, num + 1)) ** 2


def sum_of_squares(num):
    running_sum = 0
    for i in range(1, num + 1):
        running_sum += i ** 2
    return running_sum


def difference(num):
    return square_of_sum(num) - sum_of_squares(num)
