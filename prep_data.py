from __future__ import print_function

import os
import numpy as np
import pandas as pd
import tarfile
import urllib.request
import zipfile
from glob import glob

data_dir = 'data'


def flights():
    flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
    flightdir = os.path.join(data_dir, 'nycflights')
    jsondir = os.path.join(data_dir, 'flightjson')

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        urllib.request.urlretrieve(url, flights_raw)
        print("done", flush=True)

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


def random_array():
    if os.path.exists(os.path.join('data', 'random.hdf5')):
        return

    print("Create random data for array exercise")
    import h5py

    with h5py.File(os.path.join('data', 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
        for i in range(0, 1000000000, 1000000):
            dset[i: i + 1000000] = np.random.exponential(size=1000000)


def weather(growth=3200):
    url = 'https://storage.googleapis.com/dask-tutorial-data/weather-small.zip'
    weather_zip = os.path.join('data', 'weather-small.zip')
    weather_small = os.path.join('data', 'weather-small')

    if not os.path.exists(weather_zip):
        print("Downloading weather data.")
        urllib.request.urlretrieve(url, weather_zip)

    if not os.path.exists(weather_small):
        print("Extracting to {}".format(weather_small))
        zf = zipfile.ZipFile(weather_zip)
        zf.extractall(data_dir)

    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-big')):
        os.mkdir(os.path.join('data', 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    from skimage.transform import resize
    import h5py

    for fn in filenames:
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        new_shape = tuple(s * growth // 100 for s in x.shape)

        y = resize(x, new_shape, mode='constant')

        out_fn = os.path.join('data', 'weather-big', os.path.split(fn)[-1])

        try:
            with h5py.File(out_fn) as f:
                f.create_dataset('/t2m', data=y, chunks=(500, 500))
        except:
            pass


def main():
    print("Setting up data directory")
    print("-------------------------")

    flights()
    random_array()
    weather()

    print('Finished!')


if __name__ == '__main__':
    main()
