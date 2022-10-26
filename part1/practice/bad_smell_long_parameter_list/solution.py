class Unit:

    # ...
    def __init__(self):
        self.field = (30, 30)
        self.x = 0
        self.y = 0
        self.speed = 1

    def move(self, direction):
        speed = self._get_speed()#вызыветс метод _get_speed !!!!!!

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self,state = "crawl"):
        self.state= state
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
