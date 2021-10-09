# libraries
import numpy as np
import matplotlib.pyplot as plt
#from textwrap import wrap

# Dataset
height = [24, 20, 11,9,7,6,5,4,3,3,3,3,2,2,2,2]
bars = ('Remote Sensing', 'Int J Appl Earth Obs Geoinf', 'ISPRS Journal of Photogrammetry and Remote Sensing',\
    'Remote Sensing of Environment', 'ISPRS Archives',\
        'International Journal of Remote Sensing', 'Conference Paper', 'European Journal of Remote Sensing', 'GIScience & Remote Sensing',\
        'IEEE Geoscience and Remote Sensing Letters','IEEE J Sel Top Appl Earth Obs Remote Sens',\
        'IEEE Transactions on Geoscience and Remote Sensing','Canadian Journal of Remote Sensing','Geocarto International',\
        'International Journal of Digital Earth','Sustainability')
y_pos = np.arange(len(bars))
       
# Global font size
plt.rcParams.update({'font.size': 10})

# Wrap text
#bars = [ '\n'.join(wrap(i, 42)) for i in bars ]

# Create horizontal bars
plt.barh(y_pos, height, color=(0.2, 0.4, 0.6, 0.6), height=0.6)

# Create names on the y-axis
plt.yticks(y_pos, bars)

# labels read top-to-bottom
plt.gca().invert_yaxis()

# add x-axis title with increased distance from labels
#plt.xlabel('Number of publications', labelpad=10)

# Remove y-axis ticks
plt.tick_params(left=False,bottom=False, right=False,\
                labelbottom=False)
# TODO: remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

#display the value of the bar on each bar
for i, v in enumerate(height):
    plt.text(v, i, " "+str(v), color=(0.2, 0.4, 0.6, 0.9), va='center', fontweight='bold')

# Show graphic
plt.savefig('Figure_2_Source.png', dpi=900, bbox_inches='tight')
plt.show()

