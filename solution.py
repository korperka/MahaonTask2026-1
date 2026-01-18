first = dict()
second = dict()
minn, maxx = int(input("Введите нижнюю границу")), int(input("Введите верхнюю границу"))
with open("perepis.txt", "r", encoding="utf-8") as f:
    for line in f:
        info = line.split()
        year = int(info[3].split('.')[2])

        if year < 1978:
            first[info[0]] = year

        if minn <= year <= maxx:
            second[f"{info[0]} {info[1]} {info[2]}"] = year

#a
print(f"Раньше 1978 года родились {len(first)} людей: ")
print(*first.keys(), sep=', ')

#b
print(f"В диапазоне между {minn} и {maxx} годами родились: ")
print(*second.keys(), sep=', ')