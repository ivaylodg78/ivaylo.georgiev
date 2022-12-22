from errors import InvalidHeroClass
class Hero:
    CLASSES = ("Warrior", "Mage", "Priest", "Rogue")
    def __init__(self,name,gender,classingame,primaryweapon=None,item=None):
        self.Name=name
        self.Genre=gender
        if classingame not in self.CLASSES:
            raise InvalidHeroClass()
        self.ClassInGame=classingame
        self.PrimaryWeapon=primaryweapon
        self.Item=item

    def print(self):
        print(f"Hero name - {self.Name}/n"
              f"Hero gender - {self.gender}/n"
              f"Hero calss - {self.ClassInGame}/n"
              f"{self.PrimaryWeapon.print()}/n"
              f"{self.Item.print()}")