class Animal:
    zoo_name = "Hayaton"  # Add zoo_name attribute to the Animal class

    def __init__(self, name='', hunger=0):
        self.name_ = name
        self.hunger_ = hunger

    def get_name(self):
        return self.name_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.is_hungry():
            self.hunger_ -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


class Skunk(Animal):
    def __init__(self, name='', hunger=0):
        super().__init__(name, hunger)
        self._stink_count = 6

    def talk(self):
        print("tsssss")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")


class Dragon(Animal):
    def __init__(self, name='', hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Raaaawr")


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450)
    ]

    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(animal.get_name())
        animal.talk()

    additional_animals = [
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    zoo_lst += additional_animals

    print("Zoo Name:", Animal.zoo_name)  # Access the zoo_name attribute


if __name__ == '__main__':
    main()
