class Shipment:
    def __init__(self, ship_date, source, target, distance, fuel, mass):
        self.ship_date = ship_date
        self.source = source
        self.target = target
        self.distance = distance
        self.fuel = fuel
        self.mass = mass

shipments = []
with open("travels.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.split()
        shipments.append(Shipment(int(data[0]), data[2], data[3], int(data[4]), int(data[5]), int(data[6])))

#1
days = [s.ship_date for s in shipments]
best_day = max(set(days), key=days.count)
total_mass = sum(s.mass for s in shipments if s.ship_date == best_day)

print(f"В день {best_day} перевезено {total_mass} груза")

#2
lipki_mass = sum(s.mass for s in shipments if s.source == "Липки")
print(f"Из посёлка Липки отправлено {lipki_mass} груза")

#3
first_distance = sum(s.distance for s in shipments if s.ship_date == 1)
print(f"За 1 октября суммарное расстояние - {first_distance}")

#4
sources = {}
for s in shipments:
    sources[s.source] = sources.get(s.source, 0) + s.mass

print(f"Всего разных пунктов отправления {len(sources)}: {list(sources.keys())}")
print("Масса по пунктам: ", sources)

#5
targets = {}
for s in shipments:
    targets[s.target] = targets.get(s.source, 0) + s.mass

print(f"Всего разных пунктов назначения {len(targets)}: {list(targets.keys())}")
print("Масса по пунктам: ", targets)

#6
fuel = {}
for s in shipments:
    current = fuel.get(s.target, (0, 0))
    fuel[s.target] = (current[0] + s.fuel, current[1] + 1)

best_target = max(fuel, key=lambda x: fuel[x][0] / fuel[x][1])

print(f"Пункт с максимальным средним расходом: {best_target}, его расход: {fuel[best_target][0] / fuel[best_target][1]}")