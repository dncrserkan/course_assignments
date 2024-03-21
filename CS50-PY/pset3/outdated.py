def main():
    while True:
        date = input("Date: ").title()
        
        if "/" in date:
            try:
                month, day, year = date.split("/")
            except ValueError:
                # print("numbers of variables did not match")
                continue

            try:
                month, day, year = int(month), int(day), int(year)
            except ValueError:
                # print("variables cannot be casted")
                continue
            
            if (1 <= month <= 12) and (1 <= day <= 31):
                print_date(year, month, day)
                break
        
        elif "," in date:
            try:
                month_and_day, year = date.split(", ")
                month, day = month_and_day.split(" ")
            except ValueError:
                # print("numbers of variables did not match")
                continue
            
            try:
                day, year = int(day), int(year)
            except ValueError:
                # print("variables cannot be casted")
                continue

            months = create_month_dict()
            if (month in months) and (1 <= day <= 31):
                print_date(year, months[month], day)
                break

        
def print_date(year, month, day):
    print(f"{year}-{month:02}-{day:02}")


def create_month_dict():
    months = [  "January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December" ]
    index = list(range(1, 13))
    return dict(zip(months, index))


if __name__ == "__main__":
    main()
