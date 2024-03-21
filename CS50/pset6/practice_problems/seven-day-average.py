import csv
import requests
import sys


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )

    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)
    
    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done. \n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break
    
    print(f"\nSeven-Day Averages")
        
    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)
    sys.exit(0)


def calculate(reader):
    new_cases = dict()
    previous_cases = dict()
    
    for row in reader:
        if row["state"] not in new_cases.keys():
            new_cases[row["state"]] = [int(row["cases"])]
            previous_cases[row["state"]] = [int(row["cases"])]
        else:
            new_cases[row["state"]].append(int(row["cases"]) - previous_cases[row["state"]][-1])
            previous_cases[row["state"]].append(int(row["cases"]))

            if len(new_cases[row["state"]]) > 14:
                new_cases[row["state"]].pop(0)
                previous_cases[row["state"]].pop(0)
    
    return new_cases


def comparative_averages(new_cases, states):
    for state in states:
        values = new_cases[state]
        last_week_average = sum(values[7:]) // 7
        this_week_average = sum(values[:7]) // 7
        try:
            increase = 100 * (this_week_average - last_week_average) // last_week_average
        except ZeroDivisionError:
            sys.exit(1)
        
        print(f"{state} had a 7-day average of {this_week_average} and increase of {increase}%.")


if __name__ == "__main__":
    main()
