def main():
    while True:
        try:
            weeks = int(input("Number of weeks taking CS50: "))
            hours = []
            for i in range(weeks):
                hours.append(int(input(f"Week {i} HW Hours: ")))
            output = input("Enter T for total hours, A for average hours per week: ").upper()
            if output in ["T", "A"]:
                break
        except ValueError:
            continue
    
    print("{:.1f} hours".format(calc_hours(hours, weeks, output)))



def calc_hours(hours, weeks, output):
    if output == "T":
        return sum(hours)
    else:
        return sum(hours) / weeks


if __name__ == "__main__":
    main()