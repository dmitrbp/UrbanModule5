class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor > 0:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'Этажа {new_floor} не существует')
    def __str__(self):
        return f'Имя дома:{self.name}, Этажей:{self.number_of_floors}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(str(h1))
h1.go_to(5)
print(str(h2))
h2.go_to(10)
