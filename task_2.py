# Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singleton_metaclass(type):
    __one_instance = None  # __call__ for class

    def __call__(classs, *args, **kwargs):
        if classs.__one_instance == None:
            classs.__one_instance = super(Singleton_metaclass, classs) \
                .__call__(*args, *kwargs)
        return classs.__one_instance


class Person(metaclass=Singleton_metaclass):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    bob = Person("Bob")
    print(f"Bob are you Bob? Yes am {bob.name}")
    fedor = Person("Fedor")
    print(f"Fedor are you Fedor? No am {fedor.name}")
