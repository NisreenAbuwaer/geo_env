import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
dset = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\ERA5_Data\download.nc')


# Extract the relevant variables from the dataset, including air temperature (t2m),precipitation (tp), latitude, longitude, and time. Then, convert these variables into numpy arrays for further processing:


import numpy as np
t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])


# Convert the air temperature from K to ◦C and precipitation from m h−1 to mm h−1 for more intuitive interpretation

t2m = t2m - 273.15
tp = tp * 1000



# compute the mean across the second dimension to simplify the dataset:


if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)


# Create a Pandas dataframe containing time series data for both air temperature and precipitation. Focus on the grid cell closest to the reservoir (row 3,column 2):

df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:,3,2]
df_era5['tp'] = tp[:,3,2]


# plot the time series with the following commands:



fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature [°C]', color=color)
ax1.plot(df_era5.index, df_era5['t2m'], color=color, label='Temperature')
ax1.tick_params(axis='y', labelcolor=color)

# Create a secondary y-axis for precipitation
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Precipitation [mm/h]', color=color)
ax2.plot(df_era5.index, df_era5['tp'], color=color, label='Precipitation')
ax2.tick_params(axis='y', labelcolor=color)
plt.savefig('Temp_Precipitation1.png', dpi=300)



plt.title('Temperature and Precipitation Time Series at Wadi Murwani Reservoir')
df_era5.plot()
plt.show()
plt.savefig('Temp_Precipitation2.png', dpi=300)


# average annual precipitation in mm y−1? Resample the data to annual time step and calculate the mean precipitation

annual_precip = df_era5['tp'].resample('YE').mean()*24*365.25
mean_annual_precip = np.nanmean(annual_precip)

print(f"Mean Annual Precipitation: {mean_annual_precip} mm/year")




# Part 3: Calculation of Potential Evaporation (PE)

# Inputs for the function from the hourly ERA5 data:
tmin = df_era5['t2m'].resample('D').min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values
lat = 21.25  # Latitude of Wadi Murwani reservoir
doy = df_era5['t2m'].resample('D').mean().index.dayofyear


# Compute the PE using:
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

# Plot the PE time series:
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label='Potential Evaporation')
plt.xlabel('Time')
plt.ylabel('Potential evaporation (mm d−1)')
plt.show()
plt.savefig('Updated_Potential_Evaporation.png', dpi=300)



# mean annual PE in mm year−1
pe_series = pd.Series(pe, index=ts_index[:len(pe)])


annual_mean_pe = pe_series.resample('A').mean()
mean_annual_pe = annual_mean_pe.mean()

# Print the mean annual PE
print("Mean Annual PE:", mean_annual_pe)


mean_annual_pe = np.nanmean(pe)
print("Mean Annual PE:", mean_annual_pe)


print(annual_mean_pe)


# to convert it from  mm d−1 to mm y−1

mean_annual_pe_mm_year = mean_annual_pe * 365.25
print("Mean Annual PE (mm/year):", mean_annual_pe_mm_year)



