import redis
import json

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
)

def update_team_score(team_name, new_score):
    s = r.get('teams')

    if s is not None:
        teams = json.loads(s)
    else:
        teams = []

    out = None
    for team in teams:
        if team['name'] == team_name:
            out = team

    if out is None:
        teams.append({
            'name': team_name,
            'score': new_score,
            'handicaps': [],
        })
    else:
        out['score'] = new_score

    r.set('teams', json.dumps(teams))

def add_handicap(team_name, handicap):
    s = r.get('teams')

    if s is not None:
        teams = json.loads(s)
    else:
        teams = []

    out = None
    for team in teams:
        if team['name'] == team_name:
            out = team

    if out is None:
        teams.append({
            'name': team_name,
            'score': 0,
            'handicaps': [handicap],
        })
    else:
        out['handicaps'].append(handicap)

    r.set('teams', json.dumps(teams))
