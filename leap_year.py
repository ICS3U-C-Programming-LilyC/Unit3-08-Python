#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/28/2023
# This program tells the user if the year they input is a leap year.


def main():
    # Declaring variable and getting user input.
    year_as_string = input("Enter a year: ")

    # Initiating Try catch.
    try:
        year_as_integer = int(year_as_string)

        # If statement to see if the year is % 4.
        if year_as_integer % 4 == 0:
            # Nested If statement to see if the year is % 100.
            if year_as_integer % 100 == 0:
                # Nested If statement to see if the year is % 400.
                if year_as_integer % 400 == 0:
                    print(
                        "The year {} is a leap year. It will have 366 days.".format(
                            year_as_integer
                        )
                    )

                # Nested else statement to tell the user it is not a leap year.
                else:
                    print(
                        "The year {} is not a leap year. It will have 365 days".format(
                            year_as_integer
                        )
                    )

            # Nested else statement to tell the user it is a leap year.
            else:
                print(
                    "The year {} is a leap year. It will have 366 days.".format(
                        year_as_integer
                    )
                )

        # Else statement to tell the user it is not a leap year.
        else:
            print(
                "The year {} is not a leap year. It will have 365 days".format(
                    year_as_integer
                )
            )

    # Except to catch invalid inputs.
    except:
        print("Please enter a valid input.")


if __name__ == "__main__":
    main()
