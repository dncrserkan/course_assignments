import sys
import csv


def main():
    if len(sys.argv) in [1, 2]:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    try:
        with open(infile) as inf:
            temp = []
            reader = csv.DictReader(inf)
            for row in reader:
                first, last = separate(row["name"])
                house = row["house"].strip()
                temp.append({"first":first, "last":last, "house":house})
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")

    with open(outfile, "w", newline="") as outf:
        fieldnames = ["first", "last", "house"] 
        writter = csv.DictWriter(outf, fieldnames=fieldnames)
        writter.writeheader()
        for row in temp:
            writter.writerow({"first":first, "last":last, "house":house})


def separate(text):
    lastname, name = text.split(",")
    return (name.strip(), lastname.strip())


if __name__ == "__main__":
    main()
