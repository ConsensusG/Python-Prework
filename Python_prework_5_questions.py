#Question 1

#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("ConsensusG".upper())

#--------------------------------------------------------------------------------

#Question 2
 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    num = 0
    while num<100:
        num += 1
        if num % 2 != 0:
            print(num)

print(first_odds())

#----------------------------------------------------------------------------------

#Question 3

#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    sorted_list = []
    for nums in a_list:
        sorted_list.append(nums)
    sorted_list.sort()
    print(sorted_list.pop())

list_of_numbers = [12, 89, 2, 5, 1000, 10]

max_num_in_list(list_of_numbers)    

#---------------------------------------------------------------------------------

#Question 4

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

print(is_leap_year(1003))

#----------------------------------------------------------------------------------

#Question 5

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    num_waiting_list = []
    for i in range(len(a_list) - 1):
        if a_list[i] == a_list[i + 1] - 1:
            num_waiting_list.append(a_list[i])
        else:
            return False

    if len(num_waiting_list) == len(a_list) - 1:
        return True
    else:
        return False

num_list = [2, 3, 4, 5, 6, 8]
print(is_consecutive(num_list))   

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 5 (revised)  Here is a shorter version of the code that works just the same, but I think the first version makes my intent more clear
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def is_consecutive(a_list):
    num_waiting_list = []
    for i in range(len(a_list) - 1):
        if a_list[i] == a_list[i + 1] - 1:
            num_waiting_list.append(a_list[i])
        else:
            return False

    return True

num_list = [2, 3, 4, 5, 6, 8]
print(is_consecutive(num_list))   