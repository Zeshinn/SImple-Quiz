import random, sys
RED    = ""
GREEN  = ""
YELLOW = ""
WHITE  = ""
args = sys.argv[1:]
if len(args) > 0:
    if "-help" in args:
        print("Arguments:       Description:\n-color        Turns on colorful mode\n-help       Lists every argument and how it's used")
        exit()
    if "-color" in args:
        RED    = "\033[31m"
        GREEN  = "\033[32m"
        YELLOW = "\033[33m"
        WHITE  = "\033[37m"
    

user = input("1 - Start quiz\n2 - Enter questions for the quiz\n")
if user == "1":
    question_file = open("questions.txt", "r")
    questions_and_answers = question_file.readlines()
    question_file.close()
    correct_answers = 0
    wrong_answers = 0
    random.shuffle(questions_and_answers)
    for i in questions_and_answers:
        question, answer = i.split("#")
        print(f"{YELLOW}{question}{WHITE}")
        input("Enter anything to reveal answer...")
        print(f"{GREEN}{answer}{WHITE}")
        score = input("Was your answer correct? (y/n): ")
        if score == "y":
            correct_answers += 1
        else:
            wrong_answers += 1
    print(f"Correct answers: {GREEN}{correct_answers}{WHITE}")
    print(f"Wrong answers: {RED}{wrong_answers}{WHITE}")
elif user == "2":
    question_file = open("questions.txt", "a")
    user = "y"
    while user == "y":
        question = input("Enter question: ")
        answer = input("Enter asnwer: ")
        questions_and_answer = f"{question}#{answer}"
        question_file.write(f"{questions_and_answer}\n")
        user = input("Would you like to enter more questions? (y/n): ")
    question_file.close()
