class Car:
    def __init__(self, model, max_speed, color, boost):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.boost = boost
        print('This is my car. This is', model)

    def sound(self):
        print('Beep!')

    def long_sound(self):
        print('Beep, beep!')

