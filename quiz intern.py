import time
#Welcome the user
print("Welcome to the simple Quiz game! ")
time.sleep(1)

#chances
chances = 1
print("You will have",chances, "chance to answer correctly.\nplease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question 1
question_1 = print("1) What day is canada day?\n(a) July 4\n(b) July 2\n(c) July 1\n(d) July 3\n\n ")
answer_1 ="c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        break
    else:
        print("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_1,"\n\n ")

#question 2
    question_2 = print("2) What is the capital of canada?\n(a) toronto\n(b) Montreal\n(c) Vancouver\n(d) Ottawa\n\n ")
    answer_2 ="d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score +1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2,"\n\n ")

#question 3
question_3 =print("3) What is the largest city of canada?\n(a) Quebec\n(b) Toronto\n(c) Vancouver\n(d) Winnipeg\n\n ")
answer_3 ="b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score +1
        break
    else:
       print("Incorrect!\n")
       time.sleep(0.5)
       print("The correct answer is",answer_3,"\n\n ")

time.sleep(2)
#print the score
while score >= 2:
    print("Well done! Your score was", score)
    break

while score < 2:
    print("Better luck next time! Your score was", score)
    break
#Goodbye Message
print("Thank you for playing the simple quiz game!")
              


















    

              
