from tba_helper import *
import time
import datetime
from datetime import datetime
import csv

event_key = "2015gal"

rank_headers = ["Rank", "Team", "Qual Avg", "Auto", "Container", "Coopertition", "Litter", "Tote", "Played"]

def main():
    thing = get_teams_by_event_key(event_key)

    team_numbers = []
    for thingy in thing:
        team_numbers += [thingy.get("team_number")]



    team_numbers.sort()

    print(team_numbers)

    team_stats = []
    for team_number in team_numbers:
        print("Getting stats for team " + str(team_number))
        team_events = get_events_by_team_number(team_number)
        latest_event_key = get_latest_event(team_events)
        team_stats += [get_stats_for_team_event(latest_event_key, team_number)]

    with open(event_key + "_stats.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(rank_headers)
        for stat in team_stats:
            writer.writerow(stat)
        csvfile.close()

    pass


def get_latest_event(team_events):
    latest_event_key = team_events[0].get("key")
    latest_date = None
    for team_event in team_events:
        if team_event.get("key") not in event_key:
            dt = datetime.fromtimestamp(time.mktime(time.strptime(team_event.get("start_date"), "%Y-%m-%d")))

            if latest_date is None or latest_date < dt.date():
                latest_date = dt.date()
                latest_event_key = team_event.get("key")

    return latest_event_key


def get_stats_for_team_event(event_key, team_number):
    rankings_event_rankings = get_event_rankings(event_key)
    stats = []

    for rank in rankings_event_rankings:
        if str(rank[1]) not in "Team":
            if int(rank[1]) == int(team_number):
                stats = rank
                break

    return stats


if __name__ == '__main__':
    main()