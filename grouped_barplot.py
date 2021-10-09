# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
 
# set height of bar
barsRegion = [80,38,35,7]
barsDeep = [24,5,11,8]
barsEdge = [8,3,2,3]
barsPixel = [6,2,2,2]
barsHybrid = [4,2,1,1]
 
# Set position of bar on X axis
r1 = np.arange(len(barsRegion))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Global font size
plt.rcParams.update({'font.size': 13})

# Make the plot
final1=plt.bar(r1, barsRegion, color='#de425b', width=barWidth, edgecolor='white', label='Region-based')
final2=plt.bar(r2, barsDeep, color='#ec956e', width=barWidth, edgecolor='white', label='Semantic segmentation')
final3=plt.bar(r3, barsEdge, color='#feddb4', width=barWidth, edgecolor='white', label='Edge-based')
final4=plt.bar(r4, barsPixel, color='#b4b465', width=barWidth, edgecolor='white', label='Pixel-based')
final5=plt.bar(r5, barsHybrid, color='#488f31', width=barWidth, edgecolor='white', label='Hybrid')
 
# Add xticks on the middle of the group bars
plt.ylabel('Number of publications',labelpad=10)
plt.xlabel('Segmentation method',labelpad=10)
plt.xticks([r + 0.15 + barWidth for r in range(len(barsPixel))], ['Overall', '2018', '2019', '2020'])
plt.tick_params(bottom=False)

#display the value of the bar on each bar
for bar in final1:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() +1, str(int(bar.get_height())), 
                 ha='center', color='black', fontweight='bold', fontsize=12)
for bar in final2:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() +1, str(int(bar.get_height())), 
                 ha='center', color='black', fontweight='bold', fontsize=12)
for bar in final3:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() +1, str(int(bar.get_height())), 
                 ha='center', color='black', fontweight='bold', fontsize=12)
for bar in final4:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() +1, str(int(bar.get_height())), 
                 ha='center', color='black', fontweight='bold', fontsize=12)
for bar in final5:
    plt.gca().text(bar.get_x() + bar.get_width()/2,\
                   bar.get_height() +1, str(int(bar.get_height())), 
                 ha='center', color='black', fontweight='bold', fontsize=12)

# Plot size
fig = plt.gcf()
fig.set_size_inches(13,8)

# Create legend
plt.legend()
# Show graphic
plt.savefig('Figure_7_Segmentation.png', dpi=300, bbox_inches='tight')
plt.show()
