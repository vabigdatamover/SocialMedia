#https://stackoverflow.com/questions/47339352/how-do-i-convert-this-csv-data-into-a-bar-chart

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


city_df=pd.read_csv('city.csv')
city_df.set_index('geoName')[['Joe Biden','Donald Trump']].plot.bar()
plt.ylim([0,100])
plt.xlabel('Google City Trends')
plt.tight_layout()
plt.savefig("CityTrends.png", dpi=600, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches="tight", pad_inches=0.1)

dma_df=pd.read_csv('dma.csv')
dma_df.set_index('geoName')[['Joe Biden','Donald Trump']].plot.bar()
plt.ylim([0,100])
plt.xlabel('Google DMA Trends')
plt.figure(figsize=(100,50))
plt.tight_layout()
plt.savefig("DmaTrends.png", dpi=600, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches="tight", pad_inches=0.1)


city_df=pd.read_csv('city.csv')
plt.figure(figsize=(9,6))
city_df.plot.bar(x = 'Tour', y = ['Joe Biden', 'Donald Trump'])
plt.ylim([0,100])
plt.xlabel('Google City Trends')
plt.xticks(rotation=45, fontsize = 13)

# Make fake dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
# Choose the width of each bar and their positions
width = [0.1,0.2,3,1.5,0.3]
y_pos = [0,0.3,2,4.5,5.5]
 
# Make the plot
plt.bar(y_pos, height, width=width)
plt.xticks(y_pos, bars)
plt.show()


plt.tight_layout()