# Use Python's inbuilt input() function to get the required data.

import requests
from datetime import datetime
from local import API_KEY


if __name__ == "__main__":

    starting_point = input("What is your starting point? : ")
    print("You typed in as your starting point : " + starting_point)
    destination_point = input("What is your destination point? : ")
    print("You typed in as your destination point : " + destination_point)

    print("You are travelling by : ")
    print("(1) Foot")
    print("(2) Car")
    print("(3) Public Transport")
    print("(4) Bicycle")

    mode_of_travel = str(input("Enter how you are travelling : "))
    # print(mode_of_travel)
    if mode_of_travel == "1":
        mode_of_travel = "Foot"
    elif mode_of_travel == "2":
        mode_of_travel = "Car"
    elif mode_of_travel == "3":
        mode_of_travel = "Public Transport"
    elif mode_of_travel == "4":
        mode_of_travel = "Bicycle"
    else:
        raise ValueError('The entered, is not vaild.')

    print("You are travelling by : " + mode_of_travel)


# Create a seperate function to make the API call and return the data.

def get_direction()

# Create a function to calculate the arrival time.
# arrival time = current time + duration, you can use timedelta for this.
# Create a seperate function which takes all the data as the input and writes it to a html file.
# Get the right address to enter by using Google's address auto complete
