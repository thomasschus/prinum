def find_divisors(number):
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            yield i
    yield number


def find_prime_numbers(start, stop):
    for val in range(start, stop):
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                yield val


def find_spacings(numbers: list):
    spacings = []
    for idx, number in enumerate(numbers):
        if idx == 0:
            previous_number = number
            continue
        spacings.append(number - previous_number)
        previous_number = number
    return spacings


def last_digit(number: int):
    return int(str(number)[-1])


def bin_numbers(numbers: list):
    result = {}
    for number in numbers:
        if number in result:
            result[number] += 1
        else:
            result[number] = 1
    return result


def bin_successions(numbers: list):
    result = {}
    for index, number in enumerate(numbers):
        if index == 0:
            previous_number = number
            continue
        succession = (previous_number, number)
        if succession in result:
            result[succession] += 1
        else:
            result[succession] = 1
        previous_number = number
    return result
