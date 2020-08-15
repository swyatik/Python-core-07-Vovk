class Door:
    colour = 'white'
    def __init__(self, number, status, locked):
        self.number = number
        self.status = status
        self.locked = locked
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'close'
    def is_open(self):
        return self.status == 'open'

class SecurityDoor(Door):
    colour = 'grey'
    def __init__(self, number, status, locked=False):
        super().__init__(number, status, locked)

    def open(self):
        if not self.locked:
            return
        super().open()
    def close(self):
        super().close()
        self.locked = True
    def __getattr__(self, attr):
        return getattr(self.door, attr)


door1 = SecurityDoor('1', 'open')
print(door1.status)
door1.open()
print(door1.status)
print(door1.locked)
door1.close()
print(door1.status)
print(door1.number)
print(door1.locked)
