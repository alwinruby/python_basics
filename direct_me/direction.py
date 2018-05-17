
# Create a function to calculate the arrival time.
# arrival time = current time + duration, you can use timedelta for this.
# Create a seperate function which takes all the data as the input and writes it to a html file.
# Get the right address to enter by using Google's address auto complete


# Use Python's inbuilt input() function to get the required data.

import requests
from datetime import datetime
from local import API_KEY


# Create a seperate function to make the API call and return the data.

def get_direction(starting_point, destination_point, mode_of_travel):

    starting_point = "+".join(starting_point.split(" "))

    destination_point = "+".join(destination_point.split(" "))

    request_url = 'https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&mode={2}&key={3}'.format(origin,destination,travel_mode,API_KEY)

    response = requests.get(request_url)

    data = response.json()

    if data['status'] == 'OK':
        print('OK')
        return data
    elif data['status'] == 'NOT_FOUND':
        raise ValueError('The result is not found, enter a valid origin and destination address.')
    elif data['status'] == 'MAX_ROUTE_LENGTH_EXCEEDED':
        raise ValueError('The max route length has been exceeded, enter a valid origin and destination address to travel between.')
    elif data['status'] == 'ZERO_RESULTS':
        raise Exception('No results are found for your chosen options.')



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
