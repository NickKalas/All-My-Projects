print("📝 Welcome to the Task-Manager! 📝")
tasks = []
while True:
    choice = ["1", "2", "3", "4"]
    print("\n✨ What would you like to do? ✨")
    print("🔹 1. ➕ Add Task")
    print("🔹 2. 📋 View Tasks")
    print("🔹 3. ✅ Complete a Task")
    print("🔹 4. ❌ Exit")
    print("—" * 30)  # Stylish divider
    
    user_input = input("👉 Enter your choice: ")

    if user_input in choice:
        if user_input == "1":
            new_task = input("✏️ Enter your new task: ")
            tasks.append(new_task)
            print("✅ Task added successfully!")

        elif user_input == "4":
            print("👋 Goodbye! Have a productive day! 🚀")
            break

        elif user_input == "2":
            print("\n📌 Your Current Tasks: ")
            if tasks:
                for index, task in enumerate(tasks, start=1):
                    print(f"🔸 {index}. {task}")
            else:
                print("😴 No tasks added yet!")

        elif user_input == "3":
            if tasks:
                print("\n📌 Your Tasks: ")
                for index, task in enumerate(tasks, start=1):
                    print(f"🔸 {index}. {task}")
                
                completed_task = input("✅ Enter the task number you completed: ")
                if completed_task.isdigit() and 1 <= int(completed_task) <= len(tasks):
                    removed_task = tasks.pop(int(completed_task) - 1)
                    print(f"🎉 '{removed_task}' marked as completed!")
                else:
                    print("⚠️ Invalid task number!")
            else:
                print("😴 No tasks to complete!")

    else:
        print("⚠️ Please enter a valid input!")

