from src.seminar_7.task_2 import Road


# Создать не менее двух дескрипторов для атрибутов классов,
# которые вы создали ранее в ДЗ

class Validate_input_data:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Road_check_input(Road):
    _lenght = Validate_input_data()
    _width = Validate_input_data()

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width


if __name__ == '__main__':
    road = Road_check_input(20, 5000)
    road._lenght = -100
