import random


def randomInterger(min, max):
    #Random integer
    return random.randint(min, max)


def randomOperation():
    #random choice for mathematical operation
    return random.choice(['+', '-', '*'])


def operationOutput(number1, number2, operation):
    # p is the output for mathematical operation
    p = f"{number1} {operation} {number2}"
    
    if operation == '+': 
        #sum of two numbers
        a = number1 + number2
    elif operation == '-': 
        #subtraction of two numbers
        a = number1 - number2
    else: 
        #multiplication of two numbers
        a = number1 * number2
        
    #returns expression and output
    return p, a

def math_quiz():
    count = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(int(total_questions)):
        
        #selection of random numbers for function A
        number1 = randomInterger(1, 10); 
        number2 = randomInterger(1, 6); 
        #Random mathematical operation
        operation = randomOperation()
        
        # problem stores Mathematical expression
        # ANSWER stores the output of operations from function operationOutput
        PROBLEM, ANSWER = operationOutput(number1, number2, operation)
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        
        except ValueError:
            print("Please enter a valid integer.")
              

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            count += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {count}/{int(total_questions)}")

if __name__ == "__main__":
    math_quiz()
