import json
import re

all_buildings = json.load(open('./buildings.json'))

# in Onemap's database, MRT stations take the form
# either: (NS2)
# or: (EW24 / NS1)
mrt_station_code = re.compile('\\(([A-Z]{1,2}[0-9]{1,2}(?: / )?)+\\)')

def is_station(type, s):
    return (
        '{} STATION'.format(type) in s['BUILDING'] and
        mrt_station_code.search(s['ADDRESS']) is not None
    )

def update_station(type, s):
    match = mrt_station_code.search(s['ADDRESS'])

    s.update({
        'Station': match.group(0)
    })

mrt_stations = [x for x in all_buildings if is_station('MRT', x)]

for m in mrt_stations:
    update_station('MRT', m)

print(json.dumps(mrt_stations, indent=2))
print(json.dumps(sorted([x['Station'] for x in mrt_stations]), indent=2))

with open('mrt_stations.json', 'w') as f:
    f.write(json.dumps(mrt_stations, indent=2))
