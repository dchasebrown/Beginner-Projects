def sum_for_target(numbers, target):
    num_history = set()
    for num in numbers:
        compliment = target - num
        if compliment in num_history:
            index1 = numbers.index(compliment)
            index2 = numbers.index(num)
            return([index1, index2])
        else:
            num_history.add(num)
    return False

index = sum_for_target([2,11,15,10,7,3], 9)
print(index)