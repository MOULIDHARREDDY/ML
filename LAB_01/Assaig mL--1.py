

import random


#Q1
#Count pairs sum is 10
def count_pairs_with_sum(numbers):
    pair_count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                pair_count = pair_count + 1

    return pair_count


#Q2
#Find range of real numbers
def find_range(values):
    if len(values) < 3:
        return "Range determination not possible"

    minimum = values[0]
    maximum = values[0]

    for num in values:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return maximum - minimum


#Q3
#Matrix power
def multiply_matrices(A, B):
    size = len(A)
    result = []

    for i in range(size):
        row = []
        for j in range(size):
            total = 0
            for k in range(size):
                total = total + A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result


def matrix_power(A, m):
    size = len(A)

#identitymatrix
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)

    for _ in range(m):
        result = multiply_matrices(result, A)

    return result


#Q4
#Highest occurring alphabet character
def highest_occurring_character(text):
    frequency = {}

    for ch in text:
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] = frequency[ch] + 1
            else:
                frequency[ch] = 1

    max_char = None
    max_count = 0

    for ch in frequency:
        if frequency[ch] > max_count:
            max_count = frequency[ch]
            max_char = ch

    return max_char, max_count


#Q5
#mean,median,mode of 25 randomnumbers
def calculate_statistics():
    numbers = []

    for i in range(25):
        numbers.append(random.randint(1, 10))

    numbers.sort()

# Mean
    total = 0
    for num in numbers:
        total = total + num
    mean = total / len(numbers)

# Median
    median = numbers[len(numbers) // 2]

# Mode
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] = frequency[num] + 1
        else:
            frequency[num] = 1

    mode = numbers[0]
    max_count = 0

    for num in frequency:
        if frequency[num] > max_count:
            max_count = frequency[num]
            mode = num

    return numbers, mean, median, mode


#Main Function
def main():
#Q1
    numbers_q1 = [2, 7, 4, 1, 3, 6]
    print("Q1: Number of pairs with sum 10:",
          count_pairs_with_sum(numbers_q1))

#Q2
    values_q2 = [5, 3.8, 10, 4]
    print("Q2: Range of the list:",
          find_range(values_q2))

#Q3
    matrix = [
        [1, 2],
        [3, 4]
    ]
    power = 2
    print("Q3: Matrix power result:")
    result_matrix = matrix_power(matrix, power)
    for row in result_matrix:
        print(row)

#Q4
    text = "hippopotamus"
    char, count = highest_occurring_character(text)
    print("Q4:", char, "occurs", count, "times")

#Q5
    nums, mean, median, mode = calculate_statistics()
    print("Q5: Generated numbers:", nums)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)


main()
