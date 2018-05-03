from __future__ import print_function

import os
import pandas as pd
import tarfile
import urllib.request
from glob import glob

print("Setting up data directory")
print("-------------------------")

data_dir = 'data'
flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
flightdir = os.path.join(data_dir, 'nycflights')
jsondir = os.path.join(data_dir, 'flightjson')

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

if not os.path.exists(flights_raw):
    print("- Downloading NYC Flights dataset... ", end='', flush=True)
    url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
    urllib.request.urlretrieve(url, flights_raw)


if not os.path.exists(flightdir):
    print("- Extracting flight data... ", end='', flush=True)
    tar_path = os.path.join('data', 'nycflights.tar.gz')
    with tarfile.open(tar_path, mode='r:gz') as flights:
        flights.extractall('data/')
    print("done", flush=True)

if not os.path.exists(jsondir):
    print("- Creating json data... ", end='', flush=True)
    os.mkdir(jsondir)
    for path in glob(os.path.join('data', 'nycflights', '*.csv')):
        prefix = os.path.splitext(os.path.basename(path))[0]
        # Just take the first 10000 rows for the demo
        df = pd.read_csv(path).iloc[:10000]
        df.to_json(os.path.join('data', 'flightjson', prefix + '.json'),
                   orient='records', lines=True)
    print("done", flush=True)

print("** Finished! **")
