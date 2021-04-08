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
Maybe you can find the Easter Egg. Hint: It literally just said it  """)
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
                print("The program will now end.  ")
                break
        except:
            print("An error occurred")

def addToList():
    newItem = input("Please type an integer!  ")
    myList.append(newItem)
    print(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers do you want to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?   Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

    
    
def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for number-wise  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))
    print("Your number appeared [] many times in the list".format(indexCount))

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

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

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
    mainProgram()
