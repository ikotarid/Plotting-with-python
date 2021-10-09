# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

#Wikipedia link
link = "https://en.wikipedia.org/wiki/List_of_Greek_sports_teams"

#read data
table1 = pd.read_html(link,header=0, skiprows=55)[0]
table2 = pd.read_html(link,header=0, skiprows=51)[1]

table1.rename(columns={'1981–82': 'Season', 'Olympiacos': 'Football', 'Panathinaikos': 'Basketball', 'Panathinaikos.1': 'Volleyball', 'Ethnikos Piraeus': 'Water Polo',\
                       'Ionikos Nea Filadelphia': 'League'},inplace=True)
table2.rename(columns={'1981–82': 'Season', 'Panathinaikos': 'Football', 'Panathinaikos.1': 'Basketball', 'Panathinaikos.2':'Volleyball', 'not held':'Water Polo',\
                       'Unnamed: 5':'Cup'},inplace=True)

#clean data
table1.drop(table1.columns [1:5], axis = 1, inplace = True)
table2.drop(table2.columns [1:5], axis = 1, inplace = True)

table1['Season'] = [x.strip()[0:4] for x in table1['Season']]
table1['Season'] = pd.to_numeric(table1['Season'])
table1['Season'] = table1['Season']+1

table2['Season'] = [x.strip()[0:4] for x in table2['Season']]
table2['Season'] = pd.to_numeric(table2['Season'])
table2['Season'] = table2['Season']+1

table1.rename(columns={'Season': 'Number of Titles'},inplace=True)
table2.rename(columns={'Season': 'Number of Titles'},inplace=True)

G1=table1.groupby(['League']).count().nlargest(2,'Number of Titles')
G2=table2.groupby(['Cup']).count().nlargest(2,'Number of Titles')

bars1=G1['Number of Titles']
bars2=G2['Number of Titles']

# The position of the bars on the x-axis
r = [0,1]

# Names of group and bar width
names = ['Filippos Veria','Ionikos Nea Filadelphia']
barWidth = 0.5

# Create League bars
final1=plt.bar(r, bars1, color='dodgerblue', edgecolor='white', width=barWidth,label="League Titles")

# Create Cup bars on top of the firs ones
final2=plt.bar(r, bars2, bottom=bars1, color='crimson', edgecolor='white', width=barWidth,label="Cup Titles")

# y-axis in bold
plt.yticks([])
plt.ylabel("Number of Titles",fontsize=12)

# Custom X axis
plt.xticks(r, names, fontsize=12, fontweight='bold')
plt.xlabel("Handball teams", fontsize=12, labelpad=10)

# Remove x-axis ticks
plt.tick_params(bottom=False)

# Set title
plt.title("The 2 most successful teams in Greek Handball history", fontsize=16, pad=20)

# Set legend
plt.legend(loc="best")

# Remove y-axis ticks
plt.tick_params(bottom=False)

# Remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

#display the value of the bar on each bar
for bar1,bar2 in zip(final1, final2):
    h1=bar1.get_height()
    h2=bar2.get_height()
    plt.gca().text(bar1.get_x() + bar1.get_width()/2, h1/2, str(int(bar1.get_height())), ha='center', color='w', fontweight='bold', fontsize=14)
    plt.gca().text(bar2.get_x() + bar2.get_width()/2, h1+h2/2, str(int(bar2.get_height())), ha='center', color='w', fontweight='bold', fontsize=14)

# Show graphic
plt.show()
print(G1,G2)
