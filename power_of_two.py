#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Jan 10, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the square of that number.

def main():
    # initializations
    counter = 0
    power_of_two = 0

    # Get the user number
    user_number_string = input("Enter a positive number: ")
    print()

    # catches any invaild input
    try:
        # Changing string to integer
        user_number = int(user_number_string)
        # Check to see if they inputed a postive number
        if (user_number > 0):
            # calculate the sum of all numbers from 0 to user number
            for counter in range(user_number + 1):
                power_of_two = counter ** 2
                print("{}^2 = {}".format(counter, power_of_two))
                counter = counter + 1

        else:
            print("You entered a negative number, please try again.")
    except Exception:
        print("\033[1;35;38mThis is not an integer")
    finally:
        print()
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
