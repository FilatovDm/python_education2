"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

data = {
    "Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
    "Петя": ("Палатка", "Котелок", "Топор"),
    "Саша": ("Палатка", "Котелок", "Топор", "Спирт"),
}
lst = []

res_unic = set()

for k, v in data.items():
    lst.append(set(v))

for i in range(len(lst) - 2):
    res_all = lst[i].intersection(lst[i + 1])
    res_all = res_all.intersection(lst[i + 2])
print("Вещи взяли все три друга:", *res_all)

for i in range(len(lst)):
    res_unic_tmp = res_all.symmetric_difference(lst[i])
    res_unic = res_unic.symmetric_difference(res_unic_tmp)
print("Вещи уникальны, есть только у одного друга:", *res_unic)

# Не смог решить:
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
