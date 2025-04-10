print('🧮 Welcome to Nicks Calc! 🎉 To close the program, simply type "exit" 🛑')

while True:
    Equation = input("✏️  Please enter the equation: ")
    
    if Equation.lower() == "exit":
        print("👋 Goodbye! Have a great day! 😊")
        break

    try:
        print(f"🟰 Result: {eval(Equation)} ✅")
    except Exception:
        print("⚠️ Oops! An error occurred. Please try again. 🤔")
