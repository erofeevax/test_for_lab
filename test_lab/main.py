from itertools import product

def find_summ(target):
    numbers = list(range(9, -1, -1))
    operators = ['+', '-', '']

    result = []

    for i in product(operators, repeat=len(numbers) - 1):
        equation = ''.join(str(num) + op for num, op in zip(numbers, i)) + str(numbers[-1])
        if eval(equation) == target:
            result.append(equation)

    return result
# print('Введите конечную сумму')
# target_sum = int(input())
target_sum = 200
result = find_summ(target_sum)

if result:
    print('Решения:')
    for all in result:
     print(all, '=', target_sum)
else:
    print('Решение невозможно.')
