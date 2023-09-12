def func(txt: str) -> str:
    text = ''.join([el for el in txt.lower() if txt.count(el) > 1])
    return text

print(len(set(func(input("Введите строку: ")))))
# qsd


