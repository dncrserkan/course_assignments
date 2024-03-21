import re


def main():
    print(convert(input("Hours: ")))


def convert(s=""):
    expression =r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    if matches := re.search(expression, s.strip(), re.IGNORECASE):
        f_hour, f_min, f_meridiem, s_hour, s_min, s_meridiem = matches.groups()
    else:
        raise ValueError #("Cannot find any pattern")
    
    # MISSING MERIDIEMS
    if not (f_meridiem and s_meridiem):
       raise ValueError # ("Missing meridiem")
    
    # CHECK HOURS
    f_hour, s_hour = int(f_hour), int(s_hour)   # raise ValueError itself

    if (not (0 < f_hour <= 12)) or (not(0 < s_hour <= 12)):
        raise ValueError    # ("Hours are not in range")
    
    # CHECK MINUTES
    f_min = f_min if f_min is not None else 0
    s_min = s_min if s_min is not None else 0
    
    f_min, s_min = int(f_min), int(s_min)   # raise ValueError itself

    if not(0 <= f_min <= 59 or 0 <= s_min <= 59):
        raise ValueError    # ("Minutes are not in range")

    # SET OUTPUT
    f_hour = convert_hour(f_hour, f_meridiem)
    s_hour = convert_hour(s_hour, s_meridiem)
    return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"


def convert_hour(hour, meridiem):
    if meridiem.upper() == "AM":
        return hour % 12
    if meridiem.upper() == "PM":
        return (hour % 12) + 12


if __name__ == "__main__":
    main()
