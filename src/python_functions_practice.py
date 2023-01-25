def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return int(num1/num2)
#could also use // to just return the nearest whole number and ignore any remainder.

def length_of_string(string_to_test):
    return len(string_to_test)

def join_string(first_string, second_string):
    return first_string + second_string

def add_string_as_number(string_num1, string_num2):
    return int(string_num1) + int(string_num2)

import calendar
def number_to_full_month_name(month_int):
    return calendar.month_name[month_int]
  
def number_to_short_month_name(month_int):
    return calendar.month_abbr[month_int]

#Further

def volume_of_cube(num):
    return num**3

def reverse_string(entered_text):
    return entered_text[::-1]
#If you want to reverse the words and not the text you would use:
    # entered_text_split = entered_text.split()
    # reversed_words_list = entered_text_split[::-1]
    # return " ".join(reversed_words_list)

