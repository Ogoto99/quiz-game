import json
import random

def load_quiz(filename="quiz.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["categories"]

def select_category(categories):
    print("Select a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat['name']}")
    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    option_letters = ['A', 'B', 'C', 'D']

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        choices = q['choices']
        # Shuffle choices to mix up correct answer position
        combined = list(zip(option_letters, choices))
        random.shuffle(combined)

        letter_to_choice = {letter: choice for letter, choice in combined}

        for letter, choice in combined:
            print(f"  {letter}. {choice}")

        while True:
            answer = input("Your answer (A, B, C, D): ").strip().upper()
            if answer in letter_to_choice:
                break
            else:
                print("Invalid choice. Please enter A, B, C, or D.")

        if letter_to_choice[answer] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")

    return score, len(questions)

def give_feedback(score, total):
    percent = (score / total) * 100
    print(f"\nYour score: {score} out of {total} ({percent:.2f}%)")
    if percent >= 80:
        print("Excellent!")
    elif percent >= 50:
        print("Good!")
    else:
        print("Try Again!")

def main():
    categories = load_quiz()

    while True:
        category = select_category(categories)
        print(f"\nStarting quiz on category: {category['name']}")
        score, total = run_quiz(category['questions'])
        give_feedback(score, total)

        while True:
            choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
            if choice == 'Y':
                break  # restart quiz loop
            elif choice == 'N':
                print("Thanks for playing! Goodbye.")
                return
            else:
                print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    main()
