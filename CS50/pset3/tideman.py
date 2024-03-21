import sys


MAX = 9             # Max numbers of candidates
candidates = []     # list of candidates | str
preferences = []    # preferences[i][j] is number of voters who prefer i over j | int
locked = []         # locked[i][j] means i is locked in over j | bool
pairs = []

class Pair(object):
    def __init__(self, winner, winner_score, loser, loser_score):
        self.winner = winner
        self.winner_score = winner_score
        self.loser = loser
        self.loser_score = loser_score


def main():
    # CHECK INVALID USAGE
    if len(sys.argv) < 2:
        print("Usage tideman [candidate ...]")
        sys.exit(1)
    
    if len(sys.argv) - 1 > MAX:
        print(f"Maximum number of candidates is {MAX}")
        sys.exit(2)
    
    # ADD CANDIDATES to list as instance of Candidate class
    for candidate in sys.argv[1:]:
        candidates.append(candidate)
    global candidate_count
    candidate_count = len(candidates)
    
    # CREATE locked list
    for i in range(candidate_count):
        locked.append([])
        for j in range(candidate_count):
            locked[i].append("")
            locked[i][j] = False
    
    # NUMBER OF VOTERS
    try:
        voters_count = int(input("Number of voters: "))
        if voters_count <= 0:
            print(f"Number of voters must be postive number")
            sys.exit(99)
    except ValueError:
        print("Invalid input. It must be a number")
        sys.exit(99)

    # CREATE preferences list
    for i in range(candidate_count):
        preferences.append([])
        for j in range(candidate_count):
            preferences[i].append("")
            preferences[i][j] = 0
    
    # VOTING
    # For each voter > For each rank > Record vote unless it's invalid
    for voter in range(voters_count):
        ranks = []      # clear the list for every voters
        for rank in range(candidate_count):
            name = input(f"Rank {rank+1}: ")
            if not vote(name, ranks):
                print("Invalid vote.")
                sys.exit(3)
        
        record_preferences(ranks)
        print("")

    # COUNTING
    add_pairs()
    sort_pairs()
    lock_pairs()
    print_winner()
    sys.exit(0)


def vote(name:str, ranks:list) -> bool:
    if name in candidates:
        ranks.append(candidates.index(name))
        return True
    return False


def record_preferences(ranks:list[str]) -> None:
    global preferences
    for winner in ranks:
        for loser in ranks[ranks.index(winner)+1:]:   # iterate starting from winner to the last
                preferences[winner][loser] += 1


def add_pairs() -> None:
    global pairs
    for i in range(candidate_count):
        for j in range(candidate_count):
            if preferences[i][j] > preferences[j][i]:
                pairs.append(Pair(i, preferences[i][j], j, preferences[j][i]))
            else:
                continue    # do nothing in cases equality and if its smaller


def sort_pairs() -> None:
    global pairs

    def merge_sort(anylist):
        if len(anylist) <= 1:
            return anylist

        mid = len(anylist) // 2
        left = merge_sort(anylist[:mid])
        right = merge_sort(anylist[mid:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i].winner_score >= right[j].winner_score:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged += left[i:]
        merged += right[j:]

        return merged

    pairs = merge_sort(pairs)


def makes_circle(cycle_start, loser):
    """ Helper function for lock_pairs """
    if loser == cycle_start:
        return True
    for i in range(candidate_count):
        if locked[loser][i]:
            if makes_circle(cycle_start, i):
                return True
    return False


def lock_pairs():
    global locked
    for i in range(len(pairs)):
        if not makes_circle(pairs[i].winner, pairs[i].loser):
            """ Lock the pair unless it makes a circle """
            locked[pairs[i].winner][pairs[i].loser] = True


def print_winner():
    for i in range(candidate_count):
        check_value = 0
        for j in range(candidate_count):
            if locked[j][i] == False:
                check_value += 1
                if check_value == candidate_count:
                    print(candidates[i])
                    return


if __name__ == "__main__":
    main()
