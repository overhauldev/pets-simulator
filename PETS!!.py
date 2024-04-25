import random
import time
class pet:
    def __init__(self, _name):
        self.maxHungerLevel = 100
        self.HungerDecrement = random.randint(3,10)
        self.HungerLevel = round(self.maxHungerLevel/2)
        self.name = _name
        self.happiness = 100
        self.loseHappiness = 0
    
    def calcHappiness(self):
        self.loseHappiness = 0
        self.loseHappiness += (1 / self.HungerLevel) * 100 
        self.happiness -= self.loseHappiness
        self.happiness = round(self.happiness, 1)

    def feed(self):
        feed_score = random.randint(4,12)
        self.HungerLevel += feed_score
        if self.HungerLevel > self.maxHungerLevel:
            self.HungerLevel = self.maxHungerLevel
        return feed_score
    def loseHunger(self):
        self.HungerLevel -= self.HungerDecrement
    def returnname(self):
        return self.name

class Dog(pet):
    def __init__(self, _name):
        super().__init__(_name)
        self.maxActiveness = 100
        self.activeness = random.randint(0,self.maxActiveness)
    
    def loseHappiness(self):
        super(Dog, self).calcHappiness()
        #
    #def Walk():

class Cat(pet):
    def __init__(self, _name):
        super().__init__(_name)
        self.aggression = random.randint(0, 20)
        self.angerLevel = 0
        self.MaxAggression = 100
    def growAggression(self):
        self.angerLevel += self.aggression
    def loseHappiness(self):
        super(Cat, self).calcHappiness()
        #

def main():
    ## Display menu ##
    print("\n")
    print("---- Welcome to the Pet Store! ----")
    print("\n")
    print("----       Choose a pet!       ----")
    petChoice = input("          (DOG) or (CAT): ")
    petChoice = petChoice.upper()
    # get input for cat or dog
    if petChoice == "CAT" or petChoice == "DOG":
        print("You bought a", petChoice + "!")
    else:
        petChoice = "DOG"
        print("You bought a", petChoice + "!")
    
    petsName = input("What's your pet's name? ")
    print("\n")
    playGame(petChoice, petsName)

def get_pet_name(obj_pet, name):
    pet_name = obj_pet.returnname()
    hunger = obj_pet.HungerDecrement
    if hunger <= 5:
        pet_name += " the Skinny"
    elif hunger >= 8:
        pet_name += " the Hungry"
    else:
        pet_name += " the"
    
    if hasattr(obj_pet, 'activeness'):  # Check if the pet has 'activeness' attribute
        activeness = obj_pet.activeness
        if activeness <= 20:
            pet_name += " Lazy"
        elif activeness >= 80:
            pet_name += " Energetic"
    
    if hasattr(obj_pet, 'aggression'):  # Check if the pet has 'aggression' attribute
        aggression = obj_pet.aggression
        if aggression <= 5:
            pet_name += " Peaceful"
        elif aggression >= 15:
            pet_name += " Aggressive"
    
    pet_name += f" {obj_pet.__class__.__name__}"  # Get the class name dynamically
    return pet_name
def playGame(pet, name):
    # define object and random properties
    if pet == "DOG":
        obj_pet = Dog(name)
    elif pet == "CAT":
        obj_pet = Cat(name)
    pet_name = get_pet_name(obj_pet, name)
    # Display Stats
    print(pet_name)
    print("Hunger level: ", obj_pet.HungerLevel, "/", obj_pet.maxHungerLevel)
    print("Hunger Decrement: ", "-" + str(obj_pet.HungerDecrement))
    if pet == "CAT":
        print("Aggression", obj_pet.aggression)
        print("Anger: ", obj_pet.angerLevel, "/", obj_pet.MaxAggression) 
    if pet == "DOG":
        print("Activeness: ", obj_pet.activeness, "/", obj_pet.maxActiveness)
    print("\n")
    time.sleep(3)
    
    # Game Loop
    while True:
        print(pet_name + "'s", "Happiness: ", obj_pet.happiness, end="")
        print("        ", "Hunger: ", obj_pet.HungerLevel, "/", "100")
        time.sleep(1.5)
        print("\n")
        print("PROMPT:")
        print(f"(FEED) OR ", end ="")
        if pet == "DOG":
            print(f"(WALK) {obj_pet.name}?")
        if pet == "CAT": 
            print(f"(PET) {obj_pet.name}?")

        decision = input()
        decision = decision.upper()
        if decision == "FEED":
            feed_pet = obj_pet.feed()
            if feed_pet <= 8:
                print(f"Unfulfilling! Hunger increased by {feed_pet}.")
            elif feed_pet >= 10:
                print(f"Scrumptious! Hunger increased by {feed_pet}!")
            else:
                print(f"Yum! Hunger increased by {feed_pet}")
            


        elif decision == "WALK" and pet == "DOG":
            print("In progress")
        elif decision == "PET" and pet == "CAT":
            print("In progress")
        else:
            print("\n")
            print(f"Typo! {pet_name} doesn't like typos!")
            print("-5 Happiness")
            print("\n")
            obj_pet.happiness -= 5
        
        print("\n")
        # Stuff to calculate
        if decision != "FEED":
            obj_pet.loseHunger()
        obj_pet.calcHappiness()

    
main()