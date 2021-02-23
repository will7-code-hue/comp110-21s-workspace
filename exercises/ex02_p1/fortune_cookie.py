"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730215151"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    fortune_cookie ()
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    from random import randint
    randint: int = randint(1,4)
    fortune1: str = ("Travel is in your future.")
    fortune2: str = ("A healthy body will benefit you for life.")
    fortune3: str = ("Everything will work out for the best.")
    fortune4: str = ("An exciting adventure awaits you.")
    if randint == 1:
        print(fortune1)
    else:
        if randint == 2:
            print(fortune2)
        if randint == 3:
            print(fortune3)
        if randint == 4:
            print(fortune4)
    return (str(randint))


if __name__ == "__main__":
    main()
