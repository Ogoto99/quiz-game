# CLI Quiz Game

A simple command-line quiz application written in Python. The quiz presents questions from various categories, shuffles questions and answer choices, and scores the user based on their answers. It also provides feedback on the user’s performance.

---

## Features

- Loads quiz questions and categories from a JSON file (`quiz.json`).
- Allows the user to select a quiz category.
- Randomizes the order of questions and the order of answer choices.
- Accepts user input for answers with validation and error handling.
- Keeps track of the user’s score.
- Provides performance feedback: "Excellent", "Good", or "Try Again".
- Allows the user to play multiple rounds or quit the game gracefully.

---

## How to Use

1. Make sure you have Python 3 installed on your machine.
2. Prepare a `quiz.json` file in the same directory as the script, structured like this:

```json
{
  "categories": [
    {
      "name": "General Knowledge",
      "questions": [
        {
          "question": "What is the capital of France?",
          "choices": ["Paris", "London", "Berlin", "Madrid"],
          "answer": "Paris"
        },
        ...
      ]
    },
    ...
  ]
}
