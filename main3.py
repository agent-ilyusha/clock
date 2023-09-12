from typing import List


def func_list() -> List[any]:
    l = list()
    for el in range(int(input('Кол-во символов: '))):
        l.append(input("Введите символ: "))
    return l


def func_shift(com: str, list_i: list) -> List[any]:
    shift = int(com[1])
    if 'b' in com.lower():
        return list_i[shift:] + list_i[:shift]

    elif 'f' in com.lower():
        return list_i[len(list_i)-shift:]+list_i[:len(list_i)-shift]


command = input('Введите команду: ')
list_input = func_list()

print(func_shift(command, list_input))
