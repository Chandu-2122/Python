print("Welcome to the abbrevations quiz!")
print("The total no.of questions is 5. Total marks: 5")
Wannaplay = input("Do you want to play the game?(yes/no) ")
if Wannaplay.lower() != "yes":
    quit()
else:
    print("Let's play the game!")
score = 0
a1 = input("What does CPU stand for?\n ")
if a1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
a2 = input("What does ALU stand for?\n ")
if a2.lower() == "arithmetic logic unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
a3 = input("What does API stand for?\n ")
if a3.lower() == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
a4 = input("What does CISC stand for?\n ")
if a4.lower() == "complex instruction set computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
a5 = input("What does TCPA stand for?\n ")
if a5.lower() == "trusted computer platform alliance":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Your score out of 5 is: ", score)

    



