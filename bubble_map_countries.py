# libraries
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Make a data frame with the GPS of a few cities:

lon=[103.82,-100.46,10.39,79.61,5.28,2.76,-53.10,-98.31,22.96,35.17,-2.86,134.49,138.03,171.49,117.24,54.27,12.07,-3.65]
lat=[36.56,40.68,51.10,22.89,52.10,46.17,-10.78,61.36,39.07,39.06,54.12,-25.73,37.59,-41.81,-2.22,32.57,42.80,40.24]
crowd=[42,16,10,8,8,6,5,5,5,5,5,4,4,4,3,3,3,3]

 
# A basic map
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
map = Basemap()
map.bluemarble()

 
# Add a marker per city of the data frame!
#m.plot(data['lat'], data['lon'], linestyle='none', marker="o", markersize=16, alpha=0.6, c="orange", markeredgecolor="black", markeredgewidth=1)
x,y = map(lon, lat)
for x1, y1, c in zip(x, y, crowd):
    # markersize is scale down by /2 (if needed)
    # need alpha<1 to get some transparency
    # red color is more appropriate
    map.plot(x1, y1, 'ro', markersize=c/1.8, alpha=0.9)
plt.savefig('Figure_3_Country.png', dpi=600, bbox_inches='tight')
plt.show()
