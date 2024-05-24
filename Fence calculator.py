# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero/n"
    while True:

        try:
                # ask the user for a number
                response = float(input(question))

                # check that the number is more than zero
                if response > 0:
                   return response
                else:
                   print(error)


        except ValueError:
             print(error)
# Main Rountine starts here


keep_going = ""
while keep_going == "":

    # Get width and height  
    width = num_check("Width: ")
    height = num_check("Height: ")

    # enter the cost per meter
    cost = int(input("Cost per meter: "))
        
    # Caculate  perimeter
    perimeter = 2 * (width + height)

    # Caculate cost
    cost = (perimeter * cost)

    # Display output
    print()
    print(f"Cost: ${cost} ")
    print(f"Perimeter: {perimeter}m ")
    
    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the perimeter calculator")
