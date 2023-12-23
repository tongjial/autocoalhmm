import pandas as pd
import sys
import os

hdf_prefix = sys.argv[1]

hdf_file = hdf_prefix+'.HDF'
df = pd.read_hdf(hdf_file)
df.to_csv(hdf_prefix+'.csv', index=False)
