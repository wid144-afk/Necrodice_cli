import random
from dice_types import NumberDie, AttackDie, WoundDie, Vehicle_Damage_Die, Vehicle_location_Die, Vehicle_Control_Die

def roll_dice(amount):
    rolls = []
    for i in range(amount):
        rolls.append(random.randint(1, 6))
    return rolls

def main():
    dice_options = {
    "number": NumberDie,
    "attack": AttackDie,
    "wound": WoundDie,
    "damage": Vehicle_Damage_Die,
    "location": Vehicle_location_Die,
    "control": Vehicle_Control_Die
}

    while True:
        try:
            raw_input = input("Enter quantity and type (e.g., '3 attack'): ")
            parts = raw_input.split() # Splits "3 attack" into ["3", "attack"]

            if len(parts) == 2:
                count = int(parts[0])
                die_type = parts[1].lower()
    
                if die_type in dice_options:
                    die = dice_options[die_type]()
                    for _ in range(count):
                        print(f"Roll: {die.roll()}")
        except ValueError:
            print("Invalid input ganger! enter in the format '3 attack'.")

main()