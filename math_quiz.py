import random
import time

OPERATORS = ["+", "-", "*"]
min_operands = 3
max_operands = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operands, max_operands)
    right = random.randint(min_operands, max_operands)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)

    print(expr)
    answer = eval(expr)
    return expr, answer

wrong = 0

input("Press any key to begin.")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()

    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        print("Wrong answer! \n")
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

accuracy = round(total_problems / (total_problems + wrong), 2) * 100

print("Quiz complete! you finished in", total_time, "seconds.")
print("Your accuracy was", accuracy, "percent.")
