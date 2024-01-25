import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

dset = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\S\N.nc')
print(dset.variables)
DEM = np.array(dset.variables["SRTMGL1_DEM"])


plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label("Elevation (m asl)")
plt.savefig("plot.png", dpi=300)
plt.show()