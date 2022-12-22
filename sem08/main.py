from Entities import hero
from errors import InvalidCommand,HeroExists

class Menu:
    hero=[]
    def print_menu(self):
        print("1. Create a new hero")
        print("2. Create a new weapon on hero")
        print("3. Create a new item on hero")
        print("4. Print all hero")
        print("5. Delete hero")
        print("6. Exit")

    def command_create_hero(self, name, gender, hr_class):
        pass

    def run(self):
        # infinite menu loop
        while True:
            self.print_menu()
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the hero name (alpha-numeric): ")
                    for i in hero:
                        if name==i.Name:
                            raise HeroExists()
                    gender = input("Enter the hero gender (alpha-numeric): ")
                    hr_class = input("Enter the hero name (alpha-numeric): ")

                    # ...

                    #  hero = self.command_create_hero(....)
                    #  hero.append()
                    # ...
                if choice == "6":
                    break
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '_main_':
    menu = Menu()
    menu.run()