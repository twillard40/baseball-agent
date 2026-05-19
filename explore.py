from pybaseball import batting_stats_bref, pitching_stats_bref

# Batting stats
stats = batting_stats_bref(2025)

# Pitching stats
pitchers = pitching_stats_bref(2025)

# Specific pitcher
degrom = pitchers[pitchers['Name'].str.contains('deGrom', case=False)]
print(degrom.to_string())

# splits
import requests

url = "https://statsapi.mlb.com/api/v1/people/660271/stats?stats=statSplits&season=2024&group=hitting"
response = requests.get(url)
data = response.json()
print(data)

#this season

import requests

url = "https://statsapi.mlb.com/api/v1/people/660271/stats?stats=statSplits&season=2024&group=hitting&sitCodes=vr,vl"
response = requests.get(url)
data = response.json()

for split in data['stats'][0]['splits']:
    print(split['split']['description'], split['stat'])

    import json

url = "https://statsapi.mlb.com/api/v1/people/660271/stats?stats=statSplits&season=2024&group=hitting&sitCodes=vr,vl"
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=2))

url = "https://statsapi.mlb.com/api/v1/meta?type=situationCodes"
response = requests.get(url)
data = response.json()
for item in data:
    print(item)