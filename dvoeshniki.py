class Bedolaga:
    def __init__(self, surname, name, grade, algebra, geometry):
        self.surname = surname
        self.name = name
        self.grade = grade
        self.algebra = algebra
        self.geometry = geometry

    def get_score(self):
        return self.algebra + self.geometry

    def __repr__(self):
        return f"{self.surname} {self.name} {self.grade} {self.algebra} {self.geometry}"

bedolagi = []
grades = set()
with open("111.txt") as f:
    for line in f:
        data = line.split()
        bedolagi.append(Bedolaga(data[0], data[1], int(data[2]), int(data[3]), int(data[4])))
        grades.add(int(data[2]))

#1
for g in grades:
    winners = [b for b in bedolagi if b.grade == g and b.get_score() == max(bedolagi, key=lambda a: a.get_score()).get_score()]

    print(f"Победители для {g}: {winners}")

#2
alg_winners = [b for b in bedolagi if b.algebra == max(bedolagi, key=lambda a: a.algebra).algebra]
geom_winners = [b for b in bedolagi if b.geometry == max(bedolagi, key=lambda a: a.geometry).geometry]

print(f"Победители по алгебре: {alg_winners}")
print(f"Победители по геометрии: {geom_winners}")