class MissingParameterError(Exception):
    pass
class InvalidParameterError(Exception):
    def __init__(self,invalid_parameter,*args):
        message=f"Invalid class parameter: {invalid_parameter}"
        super().__init__(message,*args)
class InvalidAgeError(InvalidParameterError):
    def __init__(self,age,*args):
        super().__init__(age,*args)
class InvalidAgeError(InvalidParameterError):
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
    def make_sound(self):
        print(self.name+" says "+self.sound)
    