import csv
import sys
import random


N = 1_000_000    # Number of simulations to run


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")
    
    teams = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            teams.append({"team": row["team"], "rating": int(row["rating"])})

    counts = {}
    for _ in range(N):
        winner = simulate_tournament(teams)
        winner = winner[0]["team"]
        if winner not in counts:
            counts[winner] = 1
        else:
            counts[winner] += 1
    
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_tournament(teams):
    """ return winner team. """
    while len(teams) != 1:
        teams = simulate_round(teams)
    else:
        return teams


def simulate_round(teams):
    """ Play games for all pairs of teams.
        return: list of winner teams """
    winners = []
    for i in range(0, len(teams), 2):
        if play_game(teams[i], teams[i+1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i+1])
    return winners


def play_game(team1, team2):
    """ return: True if team1 wins, False otherwise. """
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


if __name__ == "__main__":
    main()
