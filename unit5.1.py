class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# apollo = Villager("Apollo","Eagle","pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# problem2:
bones = Villager("Bones","Dog","yip yip")
print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 