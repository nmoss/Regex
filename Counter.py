
class Counter:

    def __init__(self):
        self.count = 0

    def get_next_id(self):
        x = self.count
        self.count += 1
        return x


