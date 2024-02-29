import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
dset = xr.open_dataset(r'C:\Users\abuwaenm\Downloads\ERA5_Data\download.nc')


# Convert the air temperature (’t2m’) from K to ◦C and precipitation (tp) from m/h to mm/h
dset['t2m'] = dset['t2m'] - 273.15
dset['tp'] = dset['tp'] * 1000


# Define the location of the Wadi Murwani reservoir: 22°10'35.0"N 39°34'43.4"E
selected_location = dset.sel(latitude=22.176389, longitude=39.578722, method='nearest')



# Plot the time series of temperature
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature [°C]', color=color)
ax1.plot(selected_location['time'], selected_location['t2m'], color=color, label='Temperature')
ax1.tick_params(axis='y', labelcolor=color)

# Create a secondary y-axis for precipitation
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Precipitation [mm/h]', color=color)
ax2.plot(selected_location['time'], selected_location['tp'], color=color, label='Precipitation')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Temperature and Precipitation Time Series at Wadi Murwani Reservoir')
# to show 
# plt.show()
# to save 
# plt.savefig('Temp_Precipitation.png', dpi=300)


#Resample the data to annual time step and calculate the mean precipitation



annual_precip = selected_location['tp'].resample(time='A').mean()
print("Average Annual Precipitation:", annual_precip)

# Calculate the overall average annual precipitation
overall_avg_annual_precip = annual_precip.mean().values

# Print the result

print("Overall Average Annual Precipitation:", overall_avg_annual_precip)






# Part 3: Calculation of Potential Evaporation (PE)



# Inputs for the function from the hourly ERA5 data:
tmin = selected_location['t2m'].resample(time='D').min().values
tmax = selected_location['t2m'].resample(time='D').max().values
tmean = selected_location['t2m'].resample(time='D').mean().values
lat = 22.176389  # Latitude of Wadi Murwani reservoir
doy = selected_location['time'].resample(time='D').mean().dt.dayofyear.values

# Compute PE 
import tools
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

# Plot the PE time series
time_index = pd.to_datetime(selected_location['time'].resample(time='D').mean().values)
plt.figure(figsize=(10, 6), tight_layout=True)
plt.plot(time_index, pe, label='Potential Evaporation')
plt.xlabel('Date')
plt.ylabel('PE [mm day−1]')




plt.title('Potential Evaporation Time Series')
plt.grid(True)
# plt.show()
plt.savefig('Potential_Evaporation.png', dpi=300)

# mean annual PE in mm year−1
pe_series = pd.Series(pe[:, 0], index=time_index)
annual_mean_pe = pe_series.resample('A').mean()
mean_annual_pe = annual_mean_pe.mean()

# Print the mean annual PE
print("Mean Annual PE:", mean_annual_pe)

# for each year 

# Convert PE data to a Pandas Series for resampling
pe_series = pd.Series(pe[:, 0], index=time_index[:len(pe)])

# Resample PE annually and calculate the mean
annual_mean_pe = pe_series.resample('A').mean()
mean_annual_pe = annual_mean_pe.mean()

print(annual_mean_pe)



