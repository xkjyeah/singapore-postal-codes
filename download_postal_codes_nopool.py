import requests
import time
import re
from multiprocessing import Pool


from download_postal_codes import pcode_to_data

import json

if __name__ == '__main__':
    postal_codes = range(0, 1000000)
    postal_codes = ['{0:06d}'.format(p) for p in postal_codes]

    first = True

    with open('buildings.json', 'w') as f:
        for p in postal_codes:
          buildings = pcode_to_data(p)
          buildings.sort(key=lambda x: x['SEARCHVAL'])

          for building in buildings:
            if first:
              f.write('[\n')
              first = False
            else:
              f.write(',\n')
            f.write(re.sub('^', '  ', json.dumps(building, indent=2, sort_keys=True), flags=re.MULTILINE))

        f.write(']')
          


