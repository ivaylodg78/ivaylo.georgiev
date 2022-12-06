import random as r

class MissingParameterError(Exception):
    pass
class InvalidParameterError():
    def __init__(self,invalid_parameter,*args):
        message=f"Invalid class parametre: {invalid_parameter}"
        super().__init__(message, *args)
        
class InvalidAgeError(InvalidParameterError):
    def __init__(self,age,*args):
        super().__init__(age, *args)

class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound, *args):
        super().__init__(sound, *args)

class JungleAnimal():
    def __init__(self,name,age,sound):
        self.name=name     
        self.age=age
        self.sound=sound
        if(type(self.name)!=str):
            raise InvalidParameterError(name)
        if (type(self.age) != int):
            raise InvalidParameterError(age)
        if (type(self.sound) != str):
            raise InvalidParameterError(sound)

    def make_Sound(self):
        print(self.name+" says "+self.sound)

    def print(self):
        pass

    def daily_Task(self):
        pass
class Jaguar(JungleAnimal):
    def __init__(self,name,age,sound):
        super(). __init__(name,age,sound)
        if age > 15:
             raise InvalidAgeError(age)

        if self.sound.count("r") < 2:
            raise InvalidSoundError(sound)

    def make_Sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):
        pass

    def daily_Task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >= 15:
            raise InvalidAgeError(age)
        if self.sound.count("r") < 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def print(self):
        pass

    def daily_Task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >= 15:
            raise InvalidAgeError(age)
        if self.sound.count("r") < 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_Task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
                animals.pop(i)
                break
class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >= 10:
            raise InvalidAgeError(age)
        if self.sound.count("e") < 1:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_Task(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits.")
            return fruits
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits.")
            return 0
        else:
            print(f"{self.name} the Lemur couldn't find anything to eat")
            self.make_Sound()
            self.make_Sound()
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError(age)
        if self.sound.count("e") < 1:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")
    def daily_Task(self, animals, buildings):
        for o in range(len(animals)):
            if animals[o] == self:
                if o != 0 and o != len(animals) - 1:
                    if type(animals[o + 1]) == Human or type(animals[o - 1]) == Human:
                        typeB = "Cabin"
                        buildings.append(Building(typeB))

            if o == 0:
                    if type(animals[o + 1]) == Human:
                        typeB = "Hut"
                        buildings.append(Building(typeB))
            if o == len(animals) - 1:
                    if type(animals[o - 1]) == Human:
                        typeB = "House"
                        buildings.append(Building(typeB))
class Building():
    def __init__(self, typeB):
        self.typeB = typeB
        
    def print(self):
        print(self.typeB)


fruits = 100
animals = []
buildings = []
names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    rn = r.randint(0, 9)
    agep = r.randint(7, 20)
    name = r.randint(0, len(names) - 1)
    sound = r.randint(0, len(sounds) - 1)
    try:
        if rn >= 0 and rn <= 3:
            animals.append(Lemur(names[name], agep, sounds[sound]))
        elif rn > 3 and rn <= 7:
            animals.append(Jaguar(names[name], agep, sounds[sound]))
        elif rn > 7 and rn <= 9:
            animals.append(Human(names[name], agep, sounds[sound]))
    except InvalidAgeError(age):
        print(f"{names[name]} {agep} {sounds[sound]} {InvalidAgeError()}")
    except InvalidSoundError(sound):
        print(f"{names[name]} {agep} {sounds[sound]} {InvalidSoundError()}")

        print(f"The jungle has {len(animals)} animals now")

for an in animals:
    if type(an) == Lemur:
        fruits = an.daily_Task(fruits)
    if type(an) == Jaguar:
        an.daily_Task(animals)
    if type(an) == Human:
        an.daily_Task(animals, buildings)

    print(f"The jungle has {len(animals)} animals now")
    print(fruits)
    print(animals)
    print(buildings)



             

        
