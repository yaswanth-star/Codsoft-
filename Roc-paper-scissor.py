import random
def play():
     user = int(input("choose 1 for rock 2 for scissor 3 for paper"))
     computer = random.randint(1,3)
     print(f"computer choice is : {computer}")
     if user == computer:
        print("its draw")
     elif user == 2 and computer == 0:
        print("you lose")
     elif user == 0 and computer == 2:
        print("you win")
     elif user >=3 or user <=0:
        print("invalid number you lost")
     elif computer > user :
        print("you lose")
     elif user > computer:
        print("you win")
     else:
        return 0
def play_again():
   while True:
      answer = input("do you want to play again? (yes/no)").lower().strip()
      if answer in ("yes","no"):
         return answer =="yes"
      else:
         print("invalid input.please enter 'yes' or 'no'.")
         while True:
            play()
            if not play_again():
               break