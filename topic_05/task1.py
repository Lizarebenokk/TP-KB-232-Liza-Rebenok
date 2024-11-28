import random

elements = ["stone", "scissor", "paper"]

useryou1_choice = input("Useryou1 choose /stone/scissor/paper/: ").lower()

if useryou1_choice not in elements:
    print("Error. Please choose /stone/scissor/paper/.")
else:
    usercomp2_choice = random.choice(elements)
    print(f"Usercomp2 chose: {usercomp2_choice}")

    if useryou1_choice == usercomp2_choice:
        print("Draw!")
    elif (useryou1_choice == "stone" and usercomp2_choice == "scissor") or \
         (useryou1_choice == "scissor" and usercomp2_choice == "paper") or \
         (useryou1_choice == "paper" and usercomp2_choice == "stone"):
        print("You win!")
    else:
        print("You lost!")
