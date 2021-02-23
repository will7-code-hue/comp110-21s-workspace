"""Program that outputs one of at least four random, good fortunes."""
__author__ = "730215151"
from random import randint

randint: int = randint(1,4)
print("Your fortune cookie says...")
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
        
print("Now, go spread positive vibes!")