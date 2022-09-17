# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Warrior:
    def __init__(self):
        pass

    def attack(self):
        print('Атакую')

    def defense(self):
        print('Защищаюсь')

    def move(self):
        print('Иду')


class Healer:
    def __init__(self):
        pass

    def defense(self):
        print('Защищаюсь')

    def move(self):
        print('Иду')

    def heal(self):
        print('Лечу')


class Tree:
    def __init__(self):
        pass

    def defense(self):
        print('Защищаюсь')

    def on_fire(self):
        print('Горю')


class Trap:
    def __init__(self):
        pass

    def attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()