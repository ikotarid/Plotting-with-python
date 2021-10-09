# library
import matplotlib.pyplot as plt
 
# create data
names=['LULC classification','Building extraction','New method testing',\
       'Landslide mapping','Other']
size=[50,11,7,5,27]

plt.rcParams['font.size'] = 10

 
# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')

from palettable.colorbrewer.qualitative import Pastel1_7
plt.pie(size, labels=names, autopct='%1.0f%%', pctdistance=0.85, \
        wedgeprops = { 'linewidth' : 6, 'edgecolor' : 'white' }, colors=Pastel1_7.hex_colors)
p=plt.gcf()
p.gca().add_artist(my_circle)



plt.savefig('Figure_4_Application.png', dpi=600, bbox_inches='tight')
plt.show()


