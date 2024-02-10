import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
import tools


#Load the Jeddah weather data into a Pandas dataframe
df_isd = tools.read_isd_csv(r'C:\Users\abuwaenm\Downloads\41024099999.csv')

#overview of the ISD data for Jeddah figure 
plot = df_isd.plot(title="ISD data for Jeddah")
#plt.show()
plt.savefig('JeddahISD.png', dpi=300)


#Add a new column named RH
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values,df_isd['TMP'].values)


#Calculate the HI from air temperature and relative humidity 
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)

#highest HI observed in 2023
print (df_isd.max())



#day and time when the highest HI was observed
print (df_isd.idxmax())



#What air temperature and relative humidity were observed at that specific moment

print (df_isd.loc[["2023-08-21 10:00:00"]])



#calculate the HI using daily weather data instead of hourly data

df_isd_daily = df_isd.resample('D').mean()

print (df_isd_daily)




# Plotting HI time series for 2023
plt.figure(figsize=(10, 6))  # Adjust figsize as needed
plt.plot(df_isd_daily.index, df_isd_daily['HI'], marker='o', color='blue')

# Adding title and labels
plt.title('Daily Heat Index (HI) Time Series for 2023')
plt.xlabel('Date')
plt.ylabel('Heat Index (HI)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

#plt.show()
#to save 
plt.savefig('HI_Time_Series.png', dpi=300)


# Projected warming
projected_warming = 3  # in degrees Celsius

# Apply projected warming to air temperature data
df_isd['TMP_adjusted'] = df_isd['TMP'] + projected_warming

# Recalculate Heat Index with adjusted temperature
df_isd['HI_adjusted'] = tools.gen_heat_index(df_isd['TMP_adjusted'].values, df_isd['RH'].values)

# Find the highest Heat Index value after adjustment
adjusted_hi_max = df_isd['HI_adjusted'].max()

# Calculate the increase in the highest Heat Index value
increase_in_hi_max = adjusted_hi_max - df_isd['HI'].max()

print("Original highest HI value:", df_isd['HI'].max())
print("Highest HI value after adjustment:", adjusted_hi_max)
print("Increase in highest HI value:", increase_in_hi_max)


