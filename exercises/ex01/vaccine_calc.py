"""A vaccination calculator."""

__author__ = "730215151"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime
today: datetime = datetime.today()
print(today.strftime("%B %d, %Y"))
# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight
print(future.strftime("B %d, %Y"))
Population: int = int(input("Population: "))
Doses_administered: int = int(input("Population: "))
doses_per_day: int = int(input("Doses Per Day: "))
target_percent_vaccinated: int = int(input("Target Percent Vaccinated: ")) 













print(f"We will reach { target_percent_vaccinated } vaccination in.......")