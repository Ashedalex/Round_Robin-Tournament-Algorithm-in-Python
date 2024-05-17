def generate_round_robin_schedule(teams):
    """
    Generate a round-robin schedule for the given list of teams.
    """
    if len(teams) % 2 != 0:
        teams.append("Bye")  # Add a dummy team if odd number of teams

    n = len(teams)
    schedule = []

    for round in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            home = teams[i]
            away = teams[n - 1 - i]
            if round % 2 == 0:
                round_matches.append((home, away))
            else:
                round_matches.append((away, home))
        schedule.append(round_matches)
        teams.insert(1, teams.pop())

    return schedule


def print_schedule(schedule):
    """
    Print the round-robin schedule in a readable format.
    """
    for round_number, round_matches in enumerate(schedule):
        print(f"Round {round_number + 1}:")
        for match in round_matches:
            if "Bye" not in match:
                print(f"  {match[0]} vs {match[1]}")
            else:
                print(f"  {match[0]} has a bye" if match[1] == "Bye" else f"  {match[1]} has a bye")
        print()


def main():
    """
    Main function to get user input and generate the tournament schedule.
    """
    teams = []
    print("Enter the team names (type 'done' when finished):")
    while True:
        team = input("Team name: ").strip()
        if team.lower() == "done":
            break
        if team:
            teams.append(team)

    if len(teams) < 2:
        print("At least 2 teams are required to generate a tournament schedule.")
        return

    schedule = generate_round_robin_schedule(teams)
    print_schedule(schedule)


if __name__ == "__main__":
    main()
#pool
