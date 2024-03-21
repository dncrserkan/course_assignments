###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import csv

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cows_data = {}
    with open(filename) as file:
        reader = csv.reader(file)
        for line in reader:
            # line[0] - cow's name | line[1] - weight
            cows_data[line[0]] = int(line[1])
    return cows_data


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))
    total_weight = 0
    overall_transportation = []
    turn_passengers = []
    
    while cows_copy:
        for name in list(cows_copy.keys()):
            if total_weight + cows[name] <= limit:
                turn_passengers.append(name)
                total_weight += cows[name]
                del(cows_copy[name])

        overall_transportation.append(turn_passengers)
        turn_passengers = []
        total_weight = 0
            
    if turn_passengers:
        overall_transportation.append(turn_passengers)

    return overall_transportation


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    best = [len(cows)+1, []]

    for queue in get_partitions(cows):
        queue_breaked = False
        for sequence in queue:
            sequence_breaked = False
            total_weight = 0
            for passenger in sequence:
                total_weight += cows[passenger]
                if total_weight > limit:
                    total_weight = 0
                    sequence_breaked = True
                    break
            
            if sequence_breaked:
                queue_breaked = True
                break
        
        if not queue_breaked:
            if len(queue) < best[0]:
                best[0] = len(queue)
                best[1] = queue
                queue_breaked = False
                sequence_breaked = False    

    return best[1]


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    # LOAD COWS
    filename = "ps1_cow_data_2.txt"
    cows_data = load_cows(filename)

    print()
    # GREEDY
    start = time.time()
    solution = greedy_cow_transport(cows_data)
    end = time.time()
    print("Number of trips using the greedy algorithm:", len(solution))
    print(f"Time taken by the greedy algortimh: {(end - start):.6f}")

    print()
    # BRUTE_FORCE
    start = time.time()
    solution = brute_force_cow_transport(cows_data)
    end = time.time()
    print("Number of trips using the brute-force algorithm:", len(solution))
    print(f"Time taken by the brute-force algortimh: {(end - start):.6f}")


if __name__ == "__main__":
    compare_cow_transport_algorithms()
