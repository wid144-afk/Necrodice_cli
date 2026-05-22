import random

class Die:
    def __init__(self, name, outcomes):
        self.name = name
        self.outcomes = outcomes

    def roll(self):
        roll_index = random.randint(0, len(self.outcomes) - 1)
        return self.outcomes[roll_index]

class NumberDie(Die):
    def __init__(self):
        outcomes = [1, 2, 3, 4, 5, 6]
        super().__init__("Number Die", outcomes)

class AttackDie(Die):
    def __init__(self):
        outcomes = ["1 Hit + Ammo check", "1 Hit", "1 Hit", "2 Hit", "2 Hit", "2 Hit"]
        super().__init__("Attack Die", outcomes)

class WoundDie(Die):
    def __init__(self):
        outcomes = ["Flesh Wound", "Flesh Wound", "Seriously Injured", "Seriously Injured", "Seriously Injured", "Out of Action"]
        super().__init__("Wound Die", outcomes)

class Vehicle_Damage_Die(Die):
    def __init__(self):
        outcomes = ["Glancing", "Glancing", "Glancing", "Penetrating", "Penetrating", "Catastrophic"]
        super().__init__("Vehicle Damage Die", outcomes)

class Vehicle_location_Die(Die):
    def __init__(self):
        outcomes = ["Body", "Body", "Body", "Crew", "Drive", "Engine"]
        super().__init__("Vehicle Location Die", outcomes)

class Vehicle_Control_Die(Die):
    def __init__(self):
        outcomes = ["Swerve 45°", "Swerve 45°", "Swerve 45°", "Jack-knife 90°", "Jack-knife 90°", "Roll"]
        super().__init__("Vehicle Control Die", outcomes)

# Usage
#v_die = Vehicle_location_Die()
#print(f"Rolling {v_die.name}: {v_die.roll()}")