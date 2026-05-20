import random

def roll_dice(amount):
    rolls = []
    for i in range(amount):
        rolls.append(random.randint(1, 6))
    return rolls

def main():
    while True:
        try:
            amount = int(input("How many dice do you want to roll? "))
            if amount < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    rolls = roll_dice(amount)
    print(f"You rolled: {rolls}")

main()