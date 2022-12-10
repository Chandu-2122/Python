import random
u_score = 0
c_score = 0
options = ["rock", "paper", "scissors"]
#rock:0, paper:1, scissors:2
while True:
    u_entry = input("Choose anyone to play, Rock/Paper/Scissors or enter Q to quit: ").lower()
    if u_entry == "q":
        print("Computer score:", c_score, "User score:", u_score)
        if u_score > c_score:
            print("YOU WON. CONGRATS!!!")
        if c_score > u_score:
            print("COMPUTER WON. BETTER LUCK NEXT TIME!!!")
        if u_score == c_score:
            print("IT WAS A TIE MATCH. WELL PLAYED!!!")
        break
    if u_entry not in options:
        print("Enter a proper valid option please.")
        continue
    random_choice = random.randint(0,2)
    c_entry = options[random_choice]
    print("Computer picked:", c_entry, ".")
    if u_entry == c_entry:
        continue
    else:
        if u_entry == "rock" and c_entry == "paper":
            print("Computer got a point!!!")
            c_score += 1
        if u_entry == "rock" and c_entry == "scissors":
            print("You got a point!!!")
            u_score += 1
        if c_entry == "rock" and u_entry == "paper":
            print("You got a point!!!")
            u_score += 1
        if c_entry == "rock" and u_entry == "scissors":
            print("Computer got a point!!!")
            c_score += 1
        if u_entry == "paper" and c_entry == "scissors":
            print("Computer got a point!!!")
            c_score += 1
        if c_entry == "paper" and u_entry == "scissors":
            print("You got a point!!!")
            u_score += 1
        if u_entry == "scissors" and c_entry == "rock":
            print("Computer got a point!!!")
            c_score += 1
        
        
print("Goodbye!")
        
    
