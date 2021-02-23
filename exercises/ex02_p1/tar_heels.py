"""Tar Heels exercise redux as a structured program."""

__author__ = "730215151"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    number: int = int(input("Enter an int: "))
    tar_heels (number)


def tar_heels(number: int) -> int:
    if number % 2 and 7 == 0:
        print("TAR HEELS")
    if number % 2 and 7 != 0:
        print("CAROLINA")  
    if number % 2 == 0:
        print("TAR")
    if number % 7 == 0:
        print("HEELS")
    return number

if __name__ == "__main__":
    main()
