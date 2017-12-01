#!/usr/bin/env python3
import json
import re

# Update 1 Dec 2017: OneMap has removed the station numbers from 
# their database. Therefore I have copied in the data from LTA's
# DataMall

ALL_BUILDINGS = json.load(open('./buildings.json'))

MRT_STATION_CODE = re.compile('\\(([A-Z]{1,2}[0-9]{1,2}(?: / )?)+\\)')

DATA_MALL_MRT_STATIONS = list(open('./MRT English & Chinese names.csv', 'r', encoding='utf-16'))[1:]


def extract_station_number_and_name(line):
    number, angmoh, _, _, _ = line.strip().split('\t')
    
    return {
        'Station': number,
        'Station Name': angmoh,
    }
    
def add_onemap_data(stn):
    # Kids, this is inefficient -- you should use a hashtable, especially
    # if you want to work for Google. On the other hand, our dataset is
    # small-ish so it doesn't matter
    
    # print(stn['Station Name'].upper() + ' MRT STATION')
    # print(list(filter(lambda x: (stn['Station Name'].upper() + ' MRT STATION') == x['BUILDING'], ALL_BUILDINGS)))
    
    matching_onemap_entries = [
        o for o in ALL_BUILDINGS
        if o['BUILDING'] == stn['Station Name'].upper() + ' MRT STATION'
    ]
    
    # Unfortunately, OneMap data no longer has the station line and
    # number, so we cannot positively identify which station belongs
    # to which line. Instead, I give you *all* possible stations.
    stn['Possible Locations'] = matching_onemap_entries
    
    return stn
    

if __name__ == '__main__':
    mrt_stations = map(extract_station_number_and_name, DATA_MALL_MRT_STATIONS)
    
    mrt_stations = map(add_onemap_data, mrt_stations)
    
    with open('mrt_stations.json', 'w') as f:
        f.write(json.dumps(list(mrt_stations), indent=2, sort_keys=True))
