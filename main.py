import pandas as pd
from mplsoccer import *
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("passes.csv")

df['X'] = df['X']*1.2
df['Y'] = df['Y']*.8
df['EndX'] = df['EndX']*1.2
df['EndY'] = df['EndY']*.8

#Making the soccer field
fig, ax = plt.subplots(figsize=(13.5, 0))
fig.set_facecolor("#22312b")
ax.patch.set_facecolor("#22312b")

pitch = Pitch(pitch_type='statsbomb',
              pitch_color='#22312b', line_color='#c7d5cc')

pitch.draw(ax=ax)
plt.gca().invert_yaxis()

for x in range(len(df['X'])):
    if df['Outcome'][x] == 'Successful':
        plt.plot((df['X'][x],df['EndX'][x]),(df['Y'][x],df['EndY'][x]),color='green')
        plt.scatter(df['X'][x],df['Y'][x],color='green')
    if df['Outcome'][x] == 'Unsuccessful':
        plt.plot((df['X'][x],df['EndX'][x]),(df['Y'][x],df['EndY'][x]),color='red')
        plt.scatter(df['X'][x],df['Y'][x],color='red')

plt.title('Mo Salah passes visualizor',color='white',size=20)

plt.show()