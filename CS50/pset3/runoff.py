import sys


class Candidate(object):
    def __init__(self, name, votes=0, eliminated=False):
        self.name = name
        self.votes = votes
        self.eliminated = eliminated


MAX_VOTERS = 100
MAX_CANDIDATES = 9
candidates = []     # Container are cadidate classes, lenght must be MAX_CONTAINER
preferences =[]     # Preferences[i][j][name] -> name for jth preference for voter i


def main():
    # CHECK INVALID USAGE
    if len(sys.argv) < 2:
        print("Usage: runoff [candidate ...]")
        sys.exit(1)

    if (len(sys.argv) - 1) > MAX_CANDIDATES:
        print(f"Maximum number of candidates is {MAX_CANDIDATES}")
        sys.exit(2)

    # ADD CANDIDATES to list as instance of Candidate class
    for candidate in sys.argv[1:]:
        # Instance variables are created with their names
        # so that they can be searched in candidates by name
        exec(f"{candidate} = Candidate('{candidate}')", globals())
        candidates.append(globals()[candidate])

    # NUMBER OF VOTERS
    try:
        voters_count = int(input("Number of voters: "))
        if not 0 < voters_count < MAX_VOTERS:
            print(f"Number of voters must be in range 0 to {MAX_VOTERS}")
            sys.exit(3)
    except ValueError:
        print("Invalid input. It must be a number")
        sys.exit(3)

    # VOTING
    # For each voter > For each rank > Record vote unless it's invalid
    for voter in range(voters_count):
        preferences.append([])
        for rank in range(len(candidates)):
            preferences[voter].append([])
            name = input(f"Rank {rank+1}: ")
            if not vote(voter, rank, name):
                print("Invalid vote.")
                sys.exit(4)
        print("")
    
    # COUNTING
    while True:
        # Calculate votes given remaining candidates
        tabulate()

        # Check if there is a winner
        if print_winner(voters_count):
            sys.exit(0)

        # Find the minimum number of votes
        minimum = find_min()

        # If all remaining candidates have same numbers of votes
        if is_tie(minimum):
            for candidate in candidates:
                if not candidate.eliminated:
                    print(f"{candidate.name}")
            sys.exit(0)

        # Eliminate all candidates with the least votes
        eliminate(minimum)

        # Reset vote counts back to zero
        for candidate in candidates:
            candidate.votes = 0


# FUNCTIONS
def vote(voter:int, rank:int, name:str) -> bool:
    if globals().get(name, None) in candidates:
        preferences[voter][rank] = name
        return True
    return False


def tabulate() -> None:
    for voter in preferences:
        for name in voter:
            candidate = globals()[name]
            if not candidate.eliminated:
                candidate.votes += 1
                break


def print_winner(voters_count:int) -> bool:
    for candidate in candidates:
        if candidate.votes >= ((voters_count // 2) + 1):
            print(f"{candidate.name}")
            return True
    return False


def find_min() -> int:
    current_minimum = MAX_VOTERS
    for candidate in candidates:
        if not candidate.eliminated and candidate.votes < current_minimum:
            current_minimum = candidate.votes
    return current_minimum


def is_tie(minimum:int) -> bool:
    for candidate in candidates:
        if candidate.eliminated:
            continue
        elif candidate.votes == minimum:
            continue
        else:
            return False    # at least one different number of votes
    return True


def eliminate(minimum:int) -> None:
    for candidate in candidates:
        if not candidate.eliminated and candidate.votes == minimum:
            candidate.eliminated = True


if __name__ == "__main__":
    main()
