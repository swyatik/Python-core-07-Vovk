class Door:
    def __init__(self, number, status, lock):
        self.number = number
        self.status = status
        self.lock = lock

    def open(self):
        if self.lock == 'unlocked':
            self.status = 'opened'

    def close(self):
        self.status = 'closed'

    def onlock(self):
        self.lock = 'locked'

    def unlock(self):
        self.lock = 'unlocked'

class ColouredDoor:
    def __init__(self, number, status, colour):
        self.number = number
        self.status = status
        self.colour = colour

    def open(self):
        self.status = 'opened'

    def close(self):
        self.status = 'closed'
