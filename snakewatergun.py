import random
def Snake():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose=="Water":
        print(f"Your Choice: Snake , Computer Choice:{choose}")
        print("***You Won***\n")
    elif choose=="Snake":
        print(f"Your Choice: Snake , Computer Choice:{choose}")
        print("****Draw! Try Again***\n")
    else:
        print(f"Your Choice: Snake , Computer Choice:{choose}")
        print("Computer Won\n")
def Water():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose == "Gun":
        print(f"Your Choice: Water , Computer Choice:{choose}")
        print("***You Won***\n")
    elif choose == "Water":
        print(f"Your Choice: Water , Computer Choice:{choose}")
        print("****Draw! Try Again***\n")
    else:
        print(f"Your Choice: Water , Computer Choice:{choose}")
        print("Computer Won\n")

def Gun():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose == "Snake":
        print(f"Your Choice: Gun , Computer Choice:{choose}")
        print("***You Won***\n")
    elif choose == "Gun":
        print(f"Your Choice: Gun , Computer Choice:{choose}")
        print("****Draw! Try Again***\n")
    else:
        print(f"Your Choice: Gun , Computer Choice:{choose}")
        print("Computer Won\n")

print(f"This is Snake Water Gun Game\n")
print("Developer: Ajinkya Makode.  Welcome to Snake Water Gun game!\n")
print("Game instruction: This is a Two Player game where each player chooses one object from the choice - Snake, Water, Gun. Second Player is computer\n")
print("Rules: \n\t1. Snake vs. Water: Snake drinks the water hence wins. \n\t2. Water vs. Gun: The gun will drown in water, hence a point for water \n\t3. Gun vs. Snake: Gun will kill the snake and win.\n\tIn situations where both players choose the same object, the result will be a draw.\n\n There are 10 chances to win. Winner will be announced after calculating points\n")

i=1
while(i<11):
    a=input("Enter ur choice: Snake,Water or Gun: ")
    st=a.capitalize()

    if st=="Snake":
        Snake()
    elif st=="Water":
        Water()
    elif st=="Gun":
        Gun()
    else:
        print("Invalid choice! Choose from the above only.\n")
        # break
    print(10 - i, "no. of attempt remaning")
    i+=1
if i>10:
        print("Game Over")

