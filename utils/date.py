import re
from datetime import datetime

def convert_date_format(date_str):
    pattern = r"(\d{4})年(\d{1,2})月(\d{1,2})日"
    match = re.match(pattern, date_str)
    
    if match:
        year, month, day = match.groups()
        date = datetime(int(year), int(month), int(day))
        base_date = datetime(2025, 1, 1)
        delta = date - base_date
        return delta.days if delta.days < 0 else 1
    else:
        return 1

if __name__ == "__main__":
    date_str = "2024年10月10日"
    days = convert_date_format(date_str)
    print(days)

