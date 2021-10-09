# libraries
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Dataset
values = [35,24,23,15,13,9,8,5,4,17]
bars = ('Landsat','Sentinel','WorldView','Aerial \n imagery','Gaofen',\
        'SPOT','Quickbird','Pleiades','IKONOS','Other')
x_pos = np.arange(len(bars))

# Global font size
plt.rcParams.update({'font.size': 13})

# Create bars
final=plt.bar(x_pos, values, color=(0.2, 0.4, 0.6, 0.6), width=0.6)

# Create names on the x-axis
plt.xticks(x_pos, bars)

plt.xlabel('Sensor',labelpad=10)
plt.ylabel('Number of publications',labelpad=10)

#display the value of the bar on each bar
for bar in final:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() - 2, str(int(bar.get_height())), 
                 ha='center', color='w', fontweight='bold', fontsize=12)

# Limits for the Y axis
plt.ylim(0,35)

# Plot size
fig = plt.gcf()
fig.set_size_inches(13,8)

# Show graphic
plt.savefig('Figure_5_Sensor.png', dpi=300, bbox_inches='tight')
plt.show()
