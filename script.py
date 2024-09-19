# Una clase es una manera que tenemos en programación de buscar representar un
# objeto del mundo real.


class Person:
    def __init__(
        self, age: int, weight: float, height: int, first_name: str, last_name: str
    ):
        self.age: int = age
        self.weight: int = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

    # También podemos asignar métodos a nuestras clases
    # y usarlas de la misma manera como lo haríamos con los
    # atributos

    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")


# Luego de haber definido nuestra clase, podemos empezar a usarla en otras
# partes de nuestro código.
# Esto es a lo que llamamos crear una instancia.


user = Person(25, 70, 185, "Juan Pablo", "Isaza Marin")
print(f"{user.first_name} {user.last_name} is {user.age} years old.")
user.walk()
user.run()


# Podemos crear una clase para cualquier cosa que imaginemos.


class Bottle:
    def __init__(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")

    def recycle(self):
        print("Recycling...")


water_bottle = Bottle(1000, "plastic")
water_bottle.fill()
