
def calculate_power(number: int) -> int or str:
    if num % 2 == 0:
        return 1 if num % 4 == 0 else -1

    return 'i' if num % 5 == 0 else '-i'
# qd

num = int(input('Введите число: '))
print(calculate_power(num))
