nums = [2, 1, 3, 3, 8, 9, 4, 5, 6, 7]
sorted = []


def sort():
    #sort numbers ascending order
    temp = nums
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums

if __name__ == '__main__':
    print sort()