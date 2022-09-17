# Измените класс Person так, чтобы его методы
# оперировали внутренним состоянием,
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, number_room, city_population):
        self.number_room = number_room
        self.city_population = city_population

    def get_number_room(self):
        return self.number_room

    def get_city_population(self):
        return self.city_population


city = City()
room = Room()
number_room = room.get_name()
city_population = city.population()

person = Person(number_room, city_population)
print(person.get_number_room())
print(person.get_city_population())

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
