import operator

def checkLevel(array):
    if array[1] < array[0]:
        op = operator.lt
    elif array[1] > array[0]:
        op = operator.gt
    else:
        return False    

    for i in range(1, len(array)):
        if (not op(array[i], array[i-1])):
            return False
        difference = abs(array[i] - array[i-1])
        if (difference < 1 or difference > 3):
            return False

    return True


def checkReports(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            if checkLevel([int(x) for x in line.split()]):
                sum += 1
    return sum


def main():
    print(checkReports("input"))


if __name__ == "__main__":
    main()