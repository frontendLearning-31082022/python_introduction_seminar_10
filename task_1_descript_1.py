from src.seminar_8.task_2 import Cell


# Создать не менее двух дескрипторов для атрибутов классов,
# которые вы создали ранее в ДЗ

class Validate_cell_already_destroyed:
    def __get__(self, instance, owner):
        if instance.__dict__[self.name] == None:
            raise NameError(f"object {self.__repr__()} destroyed already")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Cell_new_ver(Cell):
    quantity = Validate_cell_already_destroyed()

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __mul__(self, other):
        # not needed now
        # self.is_destroyed()

        new_cell = Cell(self.quantity * other.quantity)

        self.__del__()
        other.__del__()

        return new_cell

    def __truediv__(self, other):
        # not needed now
        # self.is_destroyed()
        new_cell = Cell(self.quantity // other.quantity)
        self.__del__()
        other.__del__()

        return new_cell


if __name__ == '__main__':
    cell_1 = Cell_new_ver(30)
    cell_2 = Cell_new_ver(25)

    new_cell = cell_1 * cell_2
    print(f"new Cell created - quantity {new_cell}")
    print(f"Two cells destroyed while process. ")

    new_cell = cell_1 / cell_2
