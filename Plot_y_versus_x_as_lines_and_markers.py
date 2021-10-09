# library and dataset
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
 
# Create data
df=pd.DataFrame({'x_val': (2000,2001,2002,2003,2004,2005,2006,2007,\
                       2008,2009,2010,2011,2012,2013,2014,2015,2016,\
                       2017,2018,2019,2020),\
                 'y_val': (67,52,82,87,115,133,128,120,262,216,200,232,287,248,326,349,345,397,586,668,696)})

# Plot size # You typically want your plot to be ~1.33x wider than tall.
fig = plt.gcf()
fig.set_size_inches(13,8)

#plot
plt.plot('x_val','y_val', data=df, marker='o',color='#546E7A', linewidth=2)

# Global font size
plt.rcParams.update({'font.size': 13})

plt.ylabel('Number of publications', labelpad=10)

# Create names on the x-axis
plt.xticks(df['x_val'],rotation=90)


plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    top=False)         # ticks along the top edge are off

# Limit the range of the plot to only where the data is.    
# Avoid unnecessary whitespace.    
plt.ylim(0, 720)    
plt.xlim(1999, 2020) 

plt.savefig("Figure_1_Number_of_publications.png",  dpi=300, bbox_inches="tight") 
plt.show()

