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
    def close_and_lock(self):
        super().close()
        self.locked = True


door1 = SecurityDoor('1', 'open')
print(door1.status)
door1.open()
print(door1.status)
door1.close_and_lock()
print(door1.status)