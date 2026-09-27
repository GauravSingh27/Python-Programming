import re

text = "Meeting on 17-Mar-2026 and 01-Jan-2027"
dates = re.findall(r'\b\d{2}-[A-Za-z]{3}-\d{4}\b', text)
print(dates)  # ['17-Mar-2026', '01-Jan-2027']
