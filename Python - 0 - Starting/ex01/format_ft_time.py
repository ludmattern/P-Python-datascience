from time import time
from datetime import datetime

current_timestamp = time()

formatted_timestamp = f"{current_timestamp:,.4f}"
scientific_notation = f"{current_timestamp:.2e}"

current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_timestamp} \
or {scientific_notation} in scientific notation")
print(formatted_date)

"""
This script displays the current date and time in two different formats:
"""
