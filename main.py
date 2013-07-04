numbers = [2, 1, 3, 3,8, 9, 4, 5, 6, 7]
sorted = []


def sort():
    temp = list(numbers)
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers

if __name__ == '__main__':
    print sort()