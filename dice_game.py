import random

roll = random.randint(1, 6)
tries = 0

print("\n" + "👋 Welcome to the Dice Guessing Game! 🎲".center(150))
print("Try to guess the number (1-6).".center(150))
print("\n" + ("─" * 80).center(150))

while True:
    guess = input("🤔 What's your guess? ")  
    tries += 1  

    print("\n" + ("─" * 80).center(150))  

    if guess.isdigit():  
        guess = int(guess)

        if guess == roll:
            print("\n" + f"🎉🎯 Congrats!!! You found the number, it was {roll} 🎯🎉".center(150))
            print(f"🔢 You guessed it in {tries} tries! 🏆".center(150))
            break  
        elif guess > roll:
            print("📉 Too high! Try guessing a bit lower. ⬇".center(150))
        else:
            print("📈 Too low! Try guessing a bit higher. ⬆".center(150))
    else:
        print("⚠ Please enter a valid number! 🔢".center(150))

print("\n" + "🎊 Thanks for playing! 🎊".center(150))
