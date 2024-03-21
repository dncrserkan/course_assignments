def main():
    temp = input("What time is it? ").strip()
    value = convert(temp)
    # value = convert_challenged(temp)

    if 7 <= value <= 8:
        print("breakfast time")
    elif 12 <= value <= 13:
        print("lunch time")
    elif 18 <= value <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    decimal = int(minute) / 60     # ..:30 -> 0.5 
    return int(hour) + decimal


def convert_challenged(time_info):
    time, meridiem = time_info.split(" ")
    
    hour, minute = time.split(":")
    decimal = int(minute) / 60      # ..:30 -> 0.5 
    hour = int(hour) % 12           # In case something like 20:00 p.m.
    
    if meridiem == "p.m.":
        hour += 12

    return hour + decimal


if __name__ == "__main__":
    main()
