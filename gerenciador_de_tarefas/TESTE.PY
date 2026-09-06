def two_sum(numbers,target):

    indices = []

    for i, number in enumerate(numbers):

        for i2, number2 in enumerate(numbers):
            resultado = number + number2
            if resultado == target and i != i2:
                indices.append([i, i2])

    print(indices)
    return indices

two_sum([1,2,3], 4)