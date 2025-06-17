# agents/editor_agent.py

def human_edit_loop(reviewed_text):
    print("\n--- HUMAN REVIEW PHASE ---")
    print("Here is the reviewed version:\n")
    print(reviewed_text[:500] + "...\n")  # Show only the first 500 characters

    while True:
        print("Choose an option:\n"
              "[1] Accept as final\n"
              "[2] Edit manually\n"
              "[3] Exit without saving")

        choice = input("Your choice: ").strip()

        if choice == "1":
            print("✅ Accepted as final version.")
            final = reviewed_text
            break
        elif choice == "2":
            print("Enter your edited version below (end with a blank line):")
            print("--------------------------------------------------------")
            lines = []
            while True:
                line = input()
                if not line.strip():
                    break
                lines.append(line)
            final = "\n".join(lines)
            print("✍️ Your manual edits are saved.")
            break
        elif choice == "3":
            print("🚫 Exiting without saving.")
            exit(0)
        else:
            print("⚠️ Invalid input. Try again.")

    with open("chapter_1_final.txt", "w", encoding="utf-8") as f:
        f.write(final)

    return final
