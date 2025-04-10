import random

# Choices for the game
options = ["rock", "paper", "scissors"]

# Scores
user_score = 0
bot_score = 0

print("🎮 Welcome to Rock, Paper, Scissors!")
print("First to 5 points wins! 🏆")
print("-" * 30)

# Game loop
while user_score < 5 and bot_score < 5:
    bot_input = random.choice(options)
    user_input = input("\n👉 Rock, Paper, or Scissors? ").lower()

    if user_input in options:
        print(f"🤖 I chose: {bot_input}")

        if user_input == bot_input:
            print("😐 It's a Tie!")
        elif (user_input == "rock" and bot_input == "scissors") or \
             (user_input == "scissors" and bot_input == "paper") or \
             (user_input == "paper" and bot_input == "rock"):
            user_score += 1
            print("🎉 Nice! You won this round.")
        else:
            bot_score += 1
            print("💀 You lost this round.")

        # Display updated score
        print(f"📊 Score: You {user_score} - {bot_score} Bot")
        print("-" * 30)

    else:
        print("❌ Invalid choice! Please pick Rock, Paper, or Scissors.")

# Game Over message
if user_score == 5:
    print("🏆 Congrats! You won the game!")
else:
    print("😔 GGs, you lost! Better luck next time.")
