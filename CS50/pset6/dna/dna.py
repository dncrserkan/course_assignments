import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: dna.py data.csv sequence.txt")
        sys.exit(1)

    database = sys.argv[1]
    dna_sequence = sys.argv[2]
    db = []
    
    # Read database file into db
    try:
        with open(database, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                db.append(row)
            STR_seq = reader.fieldnames[1:]
    except FileNotFoundError:
        sys.exit(2)
    
    # Read DNA sequence file into sequence
    try:
        with open(dna_sequence, "r") as file:
            sequence = file.readline().rstrip()
    except FileNotFoundError:
        sys.exit(3)

    # Find longest match of each STR in DNA sequence
    instances = []
    for subsequence in STR_seq:
        instances.append(str(longest_match(sequence, subsequence)))

    # Check database for matching profiles
    for person in db:
        data = list(person.values())[1:]
        if data == instances:
            print(person["name"])
            sys.exit(0)
    print("No match")
    sys.exit(0)


def longest_match(sequence, subsequence):
    """ Returns lenght of longest run of subsequence in sequence. """

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run


if __name__ == "__main__":
    main()
