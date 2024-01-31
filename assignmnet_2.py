import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Open the datasets

dset1 = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')

dset2 = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')

dset3 = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')

dset4 = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')

dset5 = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')


# mean air temperature map for 1850–1900 

np.mean(dset2['tas'].sel(time=slice('18500101', '19001231')), axis=0)

# mean air temperature maps for 2071-2100

np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)
np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)
np.mean(dset5['tas'].sel(time=slice('20710101', '21001231')), axis=0)

# Renaming the means to simplfy the calling of a file

# meantassp... means mean air temperature for the specific time or ssp

meantahst = np.mean(dset2['tas'].sel(time=slice('18500101', '19001231')), axis=0)
meantassp119 = np.mean(dset3['tas'].sel(time=slice('20710101', '21001231')), axis=0)
meantassp245 = np.mean(dset4['tas'].sel(time=slice('20710101', '21001231')), axis=0)
meantassp585 = np.mean(dset5['tas'].sel(time=slice('20710101', '21001231')), axis=0)

# now Compute and visualize the temperature differences between 2071–2100 and 1850–1900 for each scenario

plt.imshow(meantahst)

#we add
plt.colorbar(label='Temperature (K)')  # Add color bar with label
plt.title('Historic Mean Air Temperature (2071–2100)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

#and we show the plot 
plt.show()

#to save 
plt.savefig('HistoricMean.png', dpi=300)

plt.imshow(meantassp119)
plt.colorbar(label='Temperature (K)')  # Add color bar with label
plt.title('SSP119 Mean Air Temperature (2071–2100)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
plt.savefig('SSP119Mean.png', dpi=300)

plt.imshow(meantassp245)
plt.colorbar(label='Temperature (K)')  # Add color bar with label
plt.title('SSP245 Mean Air Temperature (2071–2100)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
plt.savefig('SSP245Mean.png', dpi=300)

plt.imshow(meantassp585)
plt.colorbar(label='Temperature (K)')  # Add color bar with label
plt.title('SSP585 Mean Air Temperature (2071–2100)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
plt.savefig('SSP585Mean.png', dpi=300)



