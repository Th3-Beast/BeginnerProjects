# Created a more challenging Quiz Game.
# I've started to incorporate Type Annotations into my learning and projects and having to do a lot of
# research on this subject.
#This is the first project that incorporates the use of collections and still touches on the fundamentals.

# The Welcome Message
print("==========================================================")
print("||             Welcome To The Quiz Game!                ||")
print("==========================================================")
print("||                                                      ||")
print("|| - Test Your Knowledge                                ||")
print("|| - There Are 5 Question                               ||")
print("|| - Multiple Choice Answers                            ||")
print("|| - Title = IQ Legend                                  ||")
print("||                                                      ||")
print("==========================================================\n")

# Variables
questions: tuple[str, ...] = ('Which animal is known as the "King of the Jungle"? ',
                              'Which planet is known as the "Red Planet"? ',
                              "How many legs does a spider have? ",
                              "What is the largest mammal in the world? ",
                              "What is the capital city of France? ")

options: tuple[tuple[str, ...], ...] = (("A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"),
                                        ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
                                        ("A. 6", "B. 8", "C. 10", "D. 12"),
                                        ("A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"),
                                        ("A. London", "B. Berlin", "C. Madrid", "D. Paris"))

answers: tuple[str, ...] = ("C", "B", "B", "B", "D")

guesses: list[str] = []

score: int = 0

question_number: int = 0

# The Main Program
for question in questions:
    print("--------------------------------------------------")
    print(question)
    for option in options[question_number]:
        print()
        print(option)

    guess: str = input("\nEnter your guess: (A, B, C, D)\n").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"The answer was {answers[question_number]}")
    question_number += 1

print("--------------------------------------------------")
print("                     RESULTS                      ")
print("--------------------------------------------------\n")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

final_percentage: int = int(score / len(questions) * 100)
print(f"Your final score is {final_percentage}%")