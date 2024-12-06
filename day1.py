# Part 1
def getDistance(list1, list2):
    if not len(list1) == len(list2):
        return -1
    list1.sort()
    list2.sort()
    difference = 0
    for i in range(len(list1)):
        difference += abs(list1[i] - list2[i])
    return difference

# Part 2
def getSimilarity(list1, list2):
    count = {}
    for num in list2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    similarity = 0
    for num in list1:
        if (num in count):
            similarity += num * count[num]
    return similarity


def processInput(filename):
    list1 = []
    list2 = []
    with open(filename) as file:
        for line in file:
            nums = line.split()
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))
    return (list1, list2)

def main():
    list1, list2 = processInput("input")
    print(getDistance(list1, list2))
    print(getSimilarity(list1, list2))


if __name__ == "__main__":
    main()