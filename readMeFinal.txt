When you run the program, you will be prompted with a welcome message asking if you would like to bring up the main menu. If you would like to use the program, input "y"
which will bring up the main menu. Y means yes, while n means no. This main menu will ask you what you would like to do. You have many different choices whether to add things to the list or to search within the list
It will ask you which route you would like to take, and it will give you a number for each option. Depending on what you want, type in that number, and only the number (not the text version of the number)
Once you input a certain option, the program will then go to a next step. This could be asking you how many integers you want in your list, or if you want your list to be sorted. It will prompt
you with different options to input, so just type in your decision exactly how it is presented in the question. So a number or y/n. When you're done with the program, it will ask you if you would like to bring
up the main menu again, or if you would like to stop running the program. Input your decision, y/n, based on the question and what you would like to do with the program.

We need to create lists and sort them because integers and numbers will be jumbled without them. For numbers to be stored, there needs to be a list that can keep all of them together
These lists also need to be sorted because it allows for numeric searching and looking for things in order. It just cleans up the space in the list.

If you don't follow the instructions carefully, the program will tell you that your input isn't valid or what you said isn't an integer. It will then re-run the main program
and will essentially start over. It won't stop working unless you specifically input the correct characters to tell it to stop.



A binary search works by continuously dividing a list in halves, that could both contain the item, until it narrows down the possible locations of what you're looking to just one.
It is an efficient algorithm for finding an item from a sorted list of items. It's requirements are that a list has actual items in it, in order to select a middle point to divide
the list in half. It's limited to searching within itself, and it cannot just immediately know the index position where something is. It needs to follow the process of
taking the input of the user (in order to determine what it is looking for) and look at each index position to see if it matches what the input was. If it doesn't match, it will
continue to look at each index position until it finds one that matches the input from the user. If there's no way to end a recursive search, then there's a risk of frying a hard drive due to
the search continuing on.

The recursive algorithm, which uses recursion to accomplish a search, takes the input of the user and searches within the unique list. If the number is found in the list, it will print back
the index position that it is at. It functions within itself, and will continue on until either the number is found or the number isn't in the list. Recursive searches are functions within
a function, which means that it works entirely within itself and continues on forever.

The iterative binary search accomplishes a search by looking through the unique list and breaks it in half. It then searches through each part of the list and returns
the value associated with what the user asked for. 
If the number at the mid position is equal to the input, then the control returns index of the middle index value by printing that the number has been found along with the index at which it was found.





The original program didn't have a very user-friendly interface. I created a function called mainMenu in the program, that essentially puts all of the original functions of the program under one
simpler function. Instead of a lot of words being shown at first, the program asks if you would like to bring up the main menu, which accesses and prints the entire program. Instead of returning an
answer and immediately printing the text in the main program, it gives space which is easier to look at.

For example, 

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
            print("Sorry, an error occured")

As shown above, if the user would like to bring up the main menu, and they input "y", then the main menu will return the mainProgram (which has all of the functions in the original program).


