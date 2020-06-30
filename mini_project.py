#Ntombekazi Sibetyu Lotto challenge Mini project

import sys

#impoting the module random to be able to generate random numbers for various distributions including intergers and floats
import random

#creating a textfile to write in
project_file = open("project_file.txt","a+")

#try statement used to tst for errors when getting the age from the user
try:
    #Getting the user's age from the user,
    age = int(input("Please enter your age\n"))

#the except value error handles the value errors
except ValueError:
    print("ValueError occured, can not covert to interger")

#handles keyboard interruption errors
except KeyboardInterrupt:
    print("KeyboardInterrupt occured")

except EOFError:
    print("EOFError occured")

#verify_age(age) function determines whether the user is old enough to play lotto
def verify_age(age):
    """
    >>> verify_age(24)          #doctest for the verify_age function
    'You can continue'
    >>> verify_age(17)
    'You are too young'
    """
#if the user's age is bigger or equal to 18, the user is old enough and they can continue to play
    if age >= 18:

        print("You can continue")

#else if the user's age is less than 18, the they are too young
    else:
        print("You are too young to play")

        #the program stops
        exit()

    return age

verify_age(age)

players_name = input("please type in your full name\n")

#initializing an empty list that will store the six numbers the user will enter
players_list = []

# user_numbers(players_array) will generate the list of the users numbers
def user_numbers(players_list):
    """
    >>> user_numbers([])
    ['3','15','33','22','41','6']

    """

#making sure that the user is asked to enters a number 6 times only
    for i in range(0,6):

        #checking for errors while  getting the six numbers from user
        try:
            #getting the number as input from the user
            players_number = int(input("Enter unique number between 1 and 49\n"))

            #checking if the players_number is not already appended in the players_array
            while players_number in players_list:

                #if it already exist in the list, ask for another number from the user
                players_number = int(input("You have already used this number!Please enter another unique number between 1 and 49\n"))

        except ValueError:
            print("ValueError occured. That was not a valid number")

        except TypeError:
            print("Inappropriate type, TypeError occured")

        except EOFError:
            print("EOFError occured")

        #adding the players_number to the players_array
        players_list.append(players_number)

    return players_list
user_numbers(players_list)

#initializing an empty array that will store the lotto numbers
lotto_list = []

#function to generate a list of 6 lotto numbers
def create_lotto_list(lotto_list):
    """
    >>> create_lotto_list([])
    ['33','2','12','29','41','8']
    """
#making sure that the fubction gives only 6 numbers
    for i in range(0,6):

        #generating the random number between 1 and 49
        number = random.randint(1,49)

        #checking when the number already exist in the lotto_array
        while number in lotto_list:
            #generating a new number
            number = random.randint(1,49)

        #adding the random number generated to the lotto_array
        lotto_list.append(number)

    return lotto_list

lotto_ticket = players_list
lotto_numbers = create_lotto_list(lotto_list)

#the function compares the numbers eentered by user in players_array and the random numbers generated in the lotto_array
def count_matches(lotto_ticket,lotto_numbers):
    """
    >>> count_matches([5,14,21,30,41,11],[20,35,14,29,41,37])
    2
    >>> count_matches([5,20,31,40,12,3],[18,23,13,17,29,9])
    0
    """

#set the number of numbers that match to 0
    number_of_matches = 0

#going through every item in the players_array
    for n in lotto_ticket:

#checking if there is any item in players_array that also exists in the lotto_array
        if n in lotto_numbers:

            #increment the number of matches everytime the above is true
            number_of_matches += 1

    return number_of_matches

right_predictions = count_matches(lotto_ticket,lotto_numbers)

#function that tells the user what prize they have won using the number of matches the user had
def assign_prize(right_predictions):
    """
    >>> assign_prize(4)
    'You won R2,384'
    >>> assign_prize(1)
    'Sorry you did not win anything
    """
    try:
        #assining the amount the user must get when they get 2 matches correct
        if right_predictions == 2:
            return "You won R20.0"

        #assining the amount the user must get when they get 2 matches correct
        if right_predictions == 3:
            return "You won R100.50"

        #assining the amount the user must get when they get 2 matches correct
        if right_predictions == 4:
            return "You won R2,384"

        #assining the amount the user must get when they get 2 matches correct
        if right_predictions == 5:
            return "You won R8,584"

        #assining the amount the user must get when they get 2 matches correct
        if right_predictions == 6:
            return "You have won R10,000,000"

        #assining the amount the user must get when they get 2 matches correct
        if right_predictions <= 1:
            return "Sorry you did not win anything"

    except TypeError:
        print("Wrong type,TypeError occured")

#making the variable type to string so that it can be written to a text file
prize = str(assign_prize(right_predictions))

lotto = str(lotto_numbers)
user = str(lotto_ticket)

#current date time in local system
from datetime import datetime

date = datetime.date(datetime.now())
try:
    #writting the users age, the user's numbers, the lotto numbers, the number
    # the user predicted correctly and the prize the user will get
    project_file.writelines("\nTodays date:"+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    project_file.writelines("\nPlayers fullname:"+players_name)
    project_file.writelines("\nToday's lotto numbers:"+lotto)
    project_file.writelines("\nThe users age is"+" "+str(age))
    project_file.writelines("\nThe users lotto numbers are:"+user)
    project_file.writelines("\nThe user got"+" "+str(right_predictions)+" "+"number(s) right")
    project_file.writelines("\n"+prize+"\n")

except FileNotFoundError:
    print("File not found")

except:
    print("An error occured")

finally:
    #closing the file
    project_file.close()

#displaying the results on the screen
print(date)
print("fullname:",players_name)
print("Player's numbers",players_list)
print("lotto numbers",lotto_numbers)
print("numbers that matched",count_matches(lotto_ticket,lotto_numbers))
print(assign_prize(right_predictions))
