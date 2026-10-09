# dice_roller.py
import random

print("🎲 Welcome to Dice Roller!")

while True:
    roll = input("\nPress Enter to roll the dice (or type 'exit' to quit): ")
    if roll.lower() == "exit":
        print("👋 Goodbye!")
        break
    number = random.randint(1, 6)
    print(f"You rolled: {number}")
