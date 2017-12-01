#!/usr/bin/env python3
import json

from mrt_lrt import DATA_MALL_MRT_STATIONS, is_mrt_station, extract_station_number_and_name, add_onemap_data

if __name__ == '__main__':
    mrt_stations = map(extract_station_number_and_name, DATA_MALL_MRT_STATIONS)
    mrt_stations = filter(is_mrt_station, mrt_stations)
    mrt_stations = map(lambda s: add_onemap_data(s, station_type='MRT'), mrt_stations)
    
    with open('mrt_stations.json', 'w') as f:
        f.write(json.dumps(list(mrt_stations), indent=2, sort_keys=True))
