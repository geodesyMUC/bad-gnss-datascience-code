from pandas import *
import matplotlib.pyplot as plt

# read in the data
df = read_csv('sample_data.csv', delimiter=',', header=0, parse_dates=['timestamp'], encoding='utf-8', na_values=['N/A', 'NaN'])

# time variables
st='2023-01-01 00:00:00'
et='2023-01-01 03:00:00'

df_st = df[(df['timestamp'] >= st) & (df['timestamp'] <= et)]

df_st['num_satellites'].fillna(0, inplace=True)

numSv = df_st['num_satellites']

# plot data number of satellites
plt.figure(figsize=(12, 6))
try:
    for i in range(len(numSv)):
        if numSv[i] < 10:
            plt.plot(df_st['timestamp'][i],numSv[i],'r.')
        elif numSv[i] < 20:
            plt.plot(df_st['timestamp'][i],numSv[i],'b.')
        elif numSv[i] > 20:
            plt.plot(df_st['timestamp'][i],numSv[i],'g.')
except:
    raise Exception('An error occurred while plotting the data.')

plt.xlabel('Time')
plt.ylabel('Number of Satellites')
plt.title('Number of Satellites Over Time')
plt.savefig('satellites_plot.png')


st_pdop = '2023-01-01 00:00:00'
et_pdop ='2023-01-01 03:00:00'

df_st_pdop = df[(df['timestamp'] >= st_pdop) & (df['timestamp'] <= et_pdop)]

df_st_pdop['pdop'].fillna(0, inplace=True)

pdopValues = df_st_pdop['pdop']

# plot data number of satellites
plt.figure(figsize=(12, 6))
try:
    plt.plot(df_st_pdop['timestamp'], pdopValues)
except:
    raise Exception('An error occurred while plotting the data.')

plt.xlabel('Time')
plt.ylabel('PDOP')
plt.title('PDOP Over Time')
plt.savefig('pdop_plot.png')
