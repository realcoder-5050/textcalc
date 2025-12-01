import time 
import random

MIN_OPERAND = 2
MAX_OPERAND = 10
OPERATORS = ["+","-", "*"]
TOTAL_PROBLEMS = 10

# this is the part that determines the problem to be solved
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expr = str(left) + " " + operators +  " " + str(right)
    answer = eval(expr)
    return expr, answer

print("Press enter to start!")


start_time = time.time()
# main loop to ask questions and iterate over total problems

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + " : " + expr + " = ")
        if guess == str(answer):
            break
stop_time = time.time()
total_time = stop_time - start_time

print(f"Welldone! you finished in {total_time:.2f} seconds")
print(f"You answered {TOTAL_PROBLEMS} too!")