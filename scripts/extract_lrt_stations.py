#!/usr/bin/env python3
import json

from mrt_lrt import DATA_MALL_MRT_STATIONS, is_mrt_station, extract_station_number_and_name, add_onemap_data

if __name__ == '__main__':
    lrt_stations = map(extract_station_number_and_name, DATA_MALL_MRT_STATIONS)
    lrt_stations = filter(lambda s: not is_mrt_station(s), lrt_stations)
    lrt_stations = map(lambda s: add_onemap_data(s, station_type='LRT'), lrt_stations)
    
    with open('lrt_stations.json', 'w') as f:
        f.write(json.dumps(list(lrt_stations), indent=2, sort_keys=True))
