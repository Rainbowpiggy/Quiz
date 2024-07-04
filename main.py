# To store player's name and score
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# To store the questions and answers for the quiz
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Questions and answers are stored in a list
list_questions = [
    "What is the name of the main character in 'Whale Rider'?\n(a) Koro\n(b) Paikea\n(c) Shilo\n(d) Kai\n",
    "What is the name of Paikea's grandfather?\n(a) Kai\n(b) Koro\n(c) Raka\n(d) Hemi\n", 
    "Who plays the role of Paikea Apirana in the movie?\n(a) Keisha Castle-Hughes\n(b) Jessica Henwick\n(c) Taika Waititi\n(d) Rena Owen\n",
    "What kind of animal plays a significant role in 'Whale Rider'?\n(a) Dolphin\n(b) Whale\n(c) Crocodile\n(d) Shark\n",
    "Where is 'Whale Rider' set?\n(a) Australia\n(b) New Zealand\n(c) Canada\n(d) Japan\n",
    "What does Paikea Apirana aspire to become in the film?\n(a) Astronaut\n(b) Pilot\n(c) Doctor\n(d) The chief of her tribe\n",
]

# Answers are stored in a list
list_questions_answers = [
    Quiz(list_questions[0], "b"),
    Quiz(list_questions[1], "b"),
    Quiz(list_questions[2], "a"),
    Quiz(list_questions[3], "b"),
    Quiz(list_questions[4], "b"),
    Quiz(list_questions[5], "d")
]

# The list of acceptable answers for yes/no
yes_parameters = ["yes", "ok", "yeah", "yup", "yea", "sure", "maybe"]
no_parameters = ["no", "nope", "nah", "no thanks", "na"]

def run_quiz(list_questions_answers):
    # Get player's name and set score to 0
    user = Player(input("What is your name?\n"), 0)
    print(f"Welcome {user.name} to the Whale Rider Quiz.\n")

    #constant
    VALID_CHOICES = ['a', 'b', 'c', 'd']

    # Ask all the questions in the quiz until it reaches the end
    for quiz in list_questions_answers:
        while True:
            user_answer = input(quiz.question).lower().strip()
            # Validate the user answer
            if len(user_answer) == 0 or len(user_answer) > 1 or user_answer not in VALID_CHOICES:
                print("Please enter a valid input (a, b, c, or d)\n")
                continue
            else:
                break

        # Add a point to user score if the answer is correct
        if user_answer == quiz.answer:
            user.score += 1
            print("Correct, Well done!\n")
        else:
            print(f"Incorrect, The answer was: {quiz.answer}\n")

    # Return user score
    print(f"You got {user.score} out of {len(list_questions_answers)}\n")

    # Calculates the percentage of the user's score
    percentage = 100 * float(user.score) / float(len(list_questions_answers))
    if percentage >= 80:
        print("Well done, you did great!")
    elif percentage >= 50:
        print("You did okay.")
    else:
        print("You did poorly.")

    # Use a loop to ensure the player enters a valid yes/no answer
    while True:
        play_again = input("Do you want to play again? (yes/no)\n").lower().strip()
        if play_again not in yes_parameters and play_again not in no_parameters:
            print("Please enter a valid answer.\n")
            continue
        elif play_again in yes_parameters:
            run_quiz(list_questions_answers)
            break
        else:
            print(f"Thank you for playing {user.name}!")
            break

# Start the quiz
run_quiz(list_questions_answers)
