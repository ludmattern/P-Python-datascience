from time import time
from datetime import now

current_timestamp = time()

formatted_timestamp = f"{current_timestamp:,.4f}"
scientific_notation = f"{current_timestamp:.2e}"

current_date = now()
formatted_date = current_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_timestamp} or {scientific_notation} in scientific notation")
print(formatted_date)

"""
Code explanation:

This script displays the current date and time in two different formats:

1. UNIX TIMESTAMP:
   - time.time() gets the number of seconds elapsed since January 1, 1970
   - The :,.4f formatting adds commas as thousand separators and 4 decimal places
   - The :.2e formatting converts to scientific notation with 2 decimal places

2. FORMATTED DATE:
   - datetime.now() gets the current date and time
   - strftime("%b %d %Y") formats the date as:
     * %b = abbreviated month name (Jan, Feb, Mar...)
     * %d = day of the month (01-31)
     * %Y = full year (2025)

The goal is to show two representations of time:
- A technical representation (timestamp) used in programming
- A human-readable representation (formatted date)
"""
