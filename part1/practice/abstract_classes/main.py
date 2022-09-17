from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):

    def start_engine(self):
        print('Катер громко затарахтел')

    def move(self):
        print('Катер быстро набирает скорость')

    def stop_engine(self):
        print('Двигатель катера чихнул напоследок и заглох')

    def stop(self):
        print('Катер остановился')


class Car(Transport):

    def start_engine(self):
        print('Машина заурчала двигателем')

    def move(self):
        print('Машина едет к цели назначения')

    def stop_engine(self):
        print('Машина стоит с заглушенным двигателем')

    def stop(self):
        print('Машина остановилась')


class Electroscooter(Transport):

    def start_engine(self):
        print('Мигнул светодиодом')

    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop_engine(self):
        print('Мигнул светодиодом дважды')

    def stop(self):
        print('Торможение об стену прошло успешно')


class Person:

    def use_transport(self, transport: (Boat, Car, Electroscooter)):
        return transport.start_engine(), transport.move(), transport.stop(), transport.stop_engine()


# код должен выполняться не выбрасывая исключений

if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)