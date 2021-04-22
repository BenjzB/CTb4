"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input ot a list
4. Pull values from specific index positions
"""

#create functions that will perform those actions above
import random
import turtle
myList = []
unique_list = []

"""
mainMenu()
Function: Takes the main program and confines it within a menu. This menu can then be called, and asks for user input whether they want
to call the main program or not.
"""
def mainMenu():
    while True:
        try:
            print("Welcome to the list application. Would you like to bring up the main menu?")
            answer = input("Type Y/N ---->  ")
            if answer == "y":
                mainProgram()
            elif answer == "n":
                print("Okay, thanks for using the program")
                break
            else:
                print("That's not an answer!")
        except:
            print("Sorry, an error occured. Try again")
"""
mainProgram()
Takes all of the functions in the program and asks the user which function they would like to utilize.
It then runs that function.
"""
def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch o' numbers
3. Return the value at an index position
4. Sort List
5. Random Choice
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print Lists
9. End Program
Maybe you can find the Easter Egg. Hint: It literally just said it

---->  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            elif choice == "maybe you can find the easter egg":
                easterEgg()
            elif choice == "Maybe you can find the Easter Egg":
                easterEgg()
            else:
                print("The program will now end. Maybe try a different input  ")
                break
        except:
            print("An error occurred")

"""
addToList()
Function: Takes the user's input, converts it to an integer, and adds it to the list.
"""
def addToList():
    newItem = input("Please type an integer!  ")
    myList.append(newItem)
    print(int(newItem))
    print(myList)

"""
addABunch()
Function: Takes the user's input for number of integers and how high those integers go. These variables go into a range,
where it goes from 0 to the number of integers the user wanted to add. It then takes the list, adds the values, and randomizes it
from the range of 0 to how high the user wanted the numbers to go.
"""
def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers do you want to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")

"""
sortList(myList)
Function: As long as the number is in the main list, then it will sort. If it's not, then it puts the value in a second list called unique_list.
It then sorts the list and asks the user if they want to see the list. It lowercases the input and returns the unique list to the user if the answer is 'y'
"""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?   Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

    
"""
indexValues()
Function: Takes the user's input for the index position they would like to look, and makes it an integer.
It prints the index position that the user input as an integer, from within the list.
"""
def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

"""
randomSearch()
Takes the main list and randomizes the values it can pick from the range 0 to the amount of numbers in the list.
It then prints that random number back to the user.
"""
def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

"""
linearSearch()
Function: Searches the number you want to search by looking at each index position and seeing if the values
matches what the user input. It then finds the value that the user wanted, and gives it back to you in the slowest way possible.
"""
def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for number-wise  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))
    print("Your number appeared [] many times in the list".format(indexCount))

"""
recursiveBinarySearch()
Function: Takes the input of the user and searches within the unique list. If the number is found in the list, it will print back
the index position that it is at. It functions within itself, and will continue on until either the number is found or the number
isn't in the list.
"""
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Oh, what luck. Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

"""
iterativeBinarySearch()
Function: Looks through the unique list and breaks it in half. It then searches through each part of the list and returns
the value associated with what the user asked for.
"""
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return - 1

"""
printLists()
Function: If the value of the unique list is the same as 0, then it will print the main list.
It asks the user if they want a sorted or unsorted list, and if they input sorted, it will return the unique list.
If they don't want a sorted list, it will return the main list.
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

"""
easterEgg()
Function: If the user types in the right series of words, then it will bring a pop-up window and draw
a smiley face. It will then return to the user saying that they found the easter egg.
"""
def easterEgg():
    smiles = turtle.Turtle()    
    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.circle(10)     #eye one

    smiles.penup()
    smiles.goto(75,150)
    smiles.pendown()
    smiles.circle(10)     #eye two

    smiles.penup()
    smiles.goto(0,0)
    smiles.pendown()
    smiles.circle(100,90)   #right smile

    smiles.penup()           
    smiles.setheading(180) # <-- look West
    smiles.goto(0,0)
    smiles.pendown()
    smiles.circle(-100,90)
    print("YESSIR, YOU FOUND THE EASTER EGG")

if __name__ == "__main__":
        mainMenu()
