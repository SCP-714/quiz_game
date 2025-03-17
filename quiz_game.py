print("welcome to the monkey house")

playing = input("Would you like to enter my home? ")

if playing.lower() != "yes":
    quit()

players_name = input("What is your name traveler?")

print("excellent " + players_name + " let us begin shall we")

answer = input(players_name+" What does GPU stand for?")
if answer == "graphical processing unit":
    print("This is corect... but don't get cocky")
else:
    print("This is not correct, pleass try again")    