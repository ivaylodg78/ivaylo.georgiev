class Item:
    def __init__(self,durability=100):
        self.Durability=durability
        
    def print(self):
        print(f"Durability - {self.Durability}")