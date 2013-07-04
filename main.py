numbers = [2, 1, 3, 3, 3, 3, 4, 5, 6, 7]
sorted = []


def sort():
    #sort numbers ascending order
    for index, number in enumerate(numbers):
        if index == 0:
            sorted.append(number)
        else:
            if number < sorted[len(sorted)-1]:
                sorted.insert(len(sorted)-1, number)
            else:
                sorted.append(number)
    return sorted

if __name__ == '__main__':
    print sort()