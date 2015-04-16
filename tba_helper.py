from tba_request import make_tba_request

def get_rankings_by_key(event_key):
    return make_tba_request("event/" + event_key + "/rankings")

def get_teams_by_event_key(event_key):
    return make_tba_request("event/" + event_key + "/teams")

def get_events_by_team_number(team_number_int):
    return make_tba_request("team/frc" + str(team_number_int) + "/events")

def get_event_rankings(event_key):
    return make_tba_request("event/" + event_key + "/rankings")