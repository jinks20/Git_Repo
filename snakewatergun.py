import random
def Snake():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose=="Water":
        print("You Won\n")
    elif choose=="Snake":
        print("Draw\n")
    else:
        print("Computer Won\n")
def Water():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose == "Gun":
        print("You Won\n")
    elif choose == "Water":
        print("Draw\n")
    else:
        print("Computer Won\n")

def Gun():
    list = ["Snake", "Water", "Gun"]
    choose = random.choice(list)
    if choose == "Snake":
        print("You Won\n")
    elif choose == "Gun":
        print("Draw\n")
    else:
        print("Computer Won\n")

print(f"This is Snake Water Gun Game\n")
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
        print("Invalid choice\n")
        # break
    print(10 - i, "no. of attempt remaning")
    i+=1
if i>10:
        print("Game Over")

