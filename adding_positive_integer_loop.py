#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if a number is negative or positive

def main():
    # input
    sum_of_all_numbers = 0

# process and output
    try:
        how_many_numbers_as_string = input("Enter how many numbers: ")
        how_many_numbers = int(how_many_numbers_as_string)
        for how_many_numbers in range(how_many_numbers):
            some_number_as_string = input("Enter in a number: ")
            some_number = int(some_number_as_string)
            sum_of_all_numbers = sum_of_all_numbers + some_number
        if some_number > 0:
            print("The sum is: " + str(sum_of_all_numbers))
    except Exception:
        print("Not a number")


if __name__ == "__main__":
    main()
