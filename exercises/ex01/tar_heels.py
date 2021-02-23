"""An exercise in remainders and boolean logic."""

__author__ = "730215151"


number: int = int(input("Enter an int: "))

if number % 2 and 7 == 0:
    print("TAR HEELS")
if number % 2 and 7 != 0:
    print("CAROLINA")  
if number % 2 == 0:
    print("TAR")
if number % 7 == 0:
    print("HEELS")
  