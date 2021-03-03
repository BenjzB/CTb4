reminderList = ["eat fruits and veggies", "drink water", "go outside", "run around", "eat healthy foods"]

if "My reminder list":
    print(reminderList)

elif "My list":
    print(reminderList)

else:
    print("I dont know this command. Maybe try my list or my reminder list")

def water_function():
  print("Half body weight in oz")

water_function()

e = 3

while e < 18:
    print(e)
    if e == 9:
        break
    e += 3

food = {
  "Fruit": "Orange",
  "Veggie": "Carrot",
  "Drink": "Water"
}

mellamo = {'que te llamas': 'Benji', 'anos tienes': 16}

print("Try: My reminder list, My list, food, mellamo")

def engineGame():
    while True:
        engineType = input("Lets play the engine game. How many horses should the engine have? If you don't want to play, check the commands above.")
        numberOfVolts = input("V6, V8, V10, or V12?    ")
        engineTotal = 0

        for x in range(0, int(numberOfVolts)):
            myEngine.append(random.randint(1, int(engineType)))
            
        print("Here is your engine: {}".format(myEngine))
        print("Your engine totals, in V, were: {}".format(sum(myEngine)))
        print("Your highest engine power was: {}".format(max(myEngine)))
        print("Your lowest engine power was: {}".format(min(myEngine)))

if __name__ == '__main__':
    engineGame()

import random


def engineGame():
    while True:
        engineBay = ['V6',
                    'V8',
                    'V10',
                    'V12']

        player1 = []
        player2 = []

        numberToGive = input("How many engines would you like me to give    ")

        try:
            random.shuffle(engineBay)
            if int(numberToDeal) > 0:
                print("I'll give {} engines to each player".format(numberToGive))
                for x in range(0, int(numberToDeal)):
                    player1.append(engineBay.pop(x))
                    player2.append(engineBay.pop(x+1))
                print(player1)
                print(player2)
            else:
                print("Negative")
        except ValueError:
            print("That's not what I was looking for")

        dealAgain = input("Would you like to play the engine game again? Y/N    ")
        if dealAgain == "n":
            break

        clearGame = input("Do you want to clear your previous game? Y/N    ")
        if clearGame == "y":
            player1.clear()
            player2.clear()

if __name__ == '__main__':
    engineGame()

