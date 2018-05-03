# Parallel Data Analysis with Dask

Materials for the [Dask tutorial at PyCon 2018](https://us.pycon.org/2018/schedule/presentation/47/).

## First Time Setup

[Install Miniconda](https://conda.io/miniconda.html) or ensure you have Python 3.6 installed on your system.

```
# Update conda
conda update -n base conda

# Clone the repository
git clone https://github.com/TomAugspurger/dask-tutorial-pycon-2018

# Enter the repository
cd dsak-tutorial-pycon-2018

# Create the environment
conda env create

# Activate the environment
conda activate dask-pycon

# TODO: labextensions?

# Start jupyterlab
jupyter lab
```

If you aren't using conda

```
# Clone the repository
git clone https://github.com/TomAugspurger/dask-tutorial-pycon-2018

# Enter the repository
cd dsak-tutorial-pycon-2018

# Create a virtualenv
python3 -m venv .env

# Activate the env
# See https://docs.python.org/3/library/venv.html#creating-virtual-environments
# For bash it's
source .env/bin/activate

# Install the dependencies
python3 -m pip install -r requirements.txt

# Start jupyterlab
jupyter lab
```

## Connect to the Cluster

We have a [pangeo](https://github.com/pangeo-data/pangeo) deployment running that'll provide everyone with their own cluster to try out Dask on some larger problems.
You can log into the cluster by going to:
